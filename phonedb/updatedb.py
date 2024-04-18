import csv
from .models import UpdatePhoneNumber, PhoneNumber


def updatedb(csv_file_path, PhoneModel, batch_size=50):
    phone_numbers = []
    with open(csv_file_path, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            phone_number = PhoneModel(
                code=row["АВС/ DEF"],
                start_range=row["От"],
                end_range=row["До"],
                operator=row["Оператор"],
                region=row["Регион"],
                gar_territory=row["Территория ГАР"],
                inn=row["ИНН"],
            )
            phone_numbers.append(phone_number)
            if len(phone_numbers) >= batch_size:
                PhoneModel.objects.bulk_create(phone_numbers)
                phone_numbers = []

        if phone_numbers:
            PhoneModel.objects.bulk_create(phone_numbers)
