from django.shortcuts import render

from cars.models import Car


def car_list_all(request):
    return render(
        request=request,
        template_name='cars/car_list_all.html'
    )
