import tempfile
import requests

from django.db.models import Q
from concurrent.futures import ThreadPoolExecutor
from .updatedb import updatedb
from .models import PhoneNumber, UpdatePhoneNumber

urls = [
    "https://opendata.digital.gov.ru/downloads/ABC-3xx.csv",
    "https://opendata.digital.gov.ru/downloads/ABC-4xx.csv",
    "https://opendata.digital.gov.ru/downloads/ABC-8xx.csv",
    "https://opendata.digital.gov.ru/downloads/DEF-9xx.csv",
]
PhoneModel = None


def download_file(url):
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    file_name = temp_file.name

    response = requests.get(url, verify=False)
    with open(file_name, "wb") as out_file:
        out_file.write(response.content)

    return file_name


def process_url(url):
    global PhoneModel
    file_path = download_file(url)
    updatedb(file_path, PhoneModel)
    print(f"{url} completed")


def apply_updates():
    q1 = PhoneNumber.objects.all()

    q2 = UpdatePhoneNumber.objects.all()

    exclude_conditions = Q()
    for field in PhoneNumber._meta.get_fields():
        exclude_conditions &= Q(**{f"{field.name}__in": q1.values_list(field.name, flat=True)})

    q2_excluded = q2.exclude(exclude_conditions)

    batch_size = 50
    new_phones = []
    for record in q2_excluded:
        phone_number = PhoneNumber(
            code=record.code,
            start_range=record.start_range,
            end_range=record.end_range,
            operator=record.operator,
            region=record.region,
            gar_territory=record.gar_territory,
            inn=record.inn,
        )
        new_phones.append(phone_number)
        if len(new_phones) >= batch_size:
            PhoneNumber.objects.bulk_create(new_phones)
            new_phones = []

    if new_phones:
        PhoneNumber.objects.bulk_create(new_phones)

    ids_to_delete = q1.exclude(exclude_conditions).values_list("id", flat=True)

    PhoneNumber.objects.filter(id__in=ids_to_delete).delete()
    q2 = UpdatePhoneNumber.objects.all()
    q2.delete()


def download_all():
    global PhoneModel
    if PhoneNumber.objects.count() == 0:
        PhoneModel = PhoneNumber
    else:
        PhoneModel = UpdatePhoneNumber

    with ThreadPoolExecutor() as executor:
        executor.map(process_url, urls)

    if PhoneModel is UpdatePhoneNumber:
        apply_updates()
