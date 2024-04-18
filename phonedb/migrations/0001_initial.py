# Generated by Django 4.2.11 on 2024-04-18 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PhoneNumber",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=3)),
                ("start_range", models.IntegerField()),
                ("end_range", models.IntegerField()),
                ("operator", models.CharField(max_length=255)),
                ("region", models.CharField(max_length=255)),
                ("gar_territory", models.CharField(max_length=255)),
                ("inn", models.CharField(max_length=25)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UpdatePhoneNumber",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=3)),
                ("start_range", models.IntegerField()),
                ("end_range", models.IntegerField()),
                ("operator", models.CharField(max_length=255)),
                ("region", models.CharField(max_length=255)),
                ("gar_territory", models.CharField(max_length=255)),
                ("inn", models.CharField(max_length=25)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
