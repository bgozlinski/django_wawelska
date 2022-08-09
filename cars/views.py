from django.shortcuts import render

from cars.models import Car


def car_list_all(request):
    cars = Car.objects.all()
    return render(
        request=request,
        template_name='cars/car_list_all.html',
        context={
            'cars': cars,
        }
    )
