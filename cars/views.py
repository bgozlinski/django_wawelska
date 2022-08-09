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


def details(request, car_id):
    car = Car.objects.get(pk=car_id)

    return render(
        request=request,
        template_name='cars/car_details.html',
        context={
            'car': car
        }
    )
