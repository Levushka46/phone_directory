import csv
from .models import PhoneNumber


def updatedb(csv_file_path, batch_size=50):
    phone_numbers = []
    with open(csv_file_path, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            phone_number = PhoneNumber(
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
                PhoneNumber.objects.bulk_create(phone_numbers)
                phone_numbers = []

        if phone_numbers:
            PhoneNumber.objects.bulk_create(phone_numbers)
