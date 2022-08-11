from django.db import models


class User(models.Model):
    user_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    user_phone_number = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Imie: {self.user_name} numer: {self.user_phone_number}'
