from django.forms import ModelForm
from cars.models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        exclude = ['car_name']
        help_texts = {
            'car_service_inspection_date': 'Uzyj formatu: YYYY-MM-DD',
            'car_technical_inspection_date': 'Uzyj formatu: YYYY-MM-DD',
        }
