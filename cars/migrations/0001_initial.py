# Generated by Django 4.1 on 2022-08-08 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_number", models.SmallIntegerField(null=True)),
                ("car_mileage", models.PositiveIntegerField(blank=True, null=True)),
                ("car_service_inspection_date", models.DateField()),
                ("car_technical_inspection_date", models.DateField()),
                ("car_content", models.TextField()),
            ],
        ),
    ]