# Generated by Django 4.1 on 2022-08-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_car_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_content',
            field=models.TextField(blank=True, verbose_name='opis'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_mileage',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Przebieg'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.SmallIntegerField(null=True, verbose_name='Numer pojazdu'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_service_inspection_date',
            field=models.DateField(blank=True, verbose_name='Data przeglądu serwisowego'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_technical_inspection_date',
            field=models.DateField(blank=True, verbose_name='Data przeglądu technicznego'),
        ),
    ]