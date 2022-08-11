from django.db import models


class Car(models.Model):
    car_number = models.SmallIntegerField(
        blank=False,
        null=True,
        verbose_name='Numer pojazdu'
    )
    car_mileage = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='Przebieg'
    )
    car_service_inspection_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data przeglądu serwisowego'
    )
    car_technical_inspection_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data przeglądu technicznego',
    )
    car_content = models.TextField(
        blank=True,
        null=True,
        verbose_name='opis'
    )

    def __str__(self):
        return f'{self.car_number}'
