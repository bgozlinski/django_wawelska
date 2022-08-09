from django.db import models


class Car(models.Model):
    car_number = models.SmallIntegerField(blank=False, null=True)
    car_mileage = models.PositiveIntegerField(blank=True, null=True)
    car_service_inspection_date = models.DateField()
    car_technical_inspection_date = models.DateField()
    car_content = models.TextField()

    def __str__(self):
        return f'{self.car_number}'
