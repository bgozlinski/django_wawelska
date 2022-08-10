from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from cars.forms import CarForm
from cars.models import Car


@login_required()
def car_list_all(request):
    cars = Car.objects.all()
    return render(
        request=request,
        template_name='cars/car_list_all.html',
        context={
            'cars': cars,
        }
    )


@login_required()
def details(request, car_id):
    car = Car.objects.get(pk=car_id)

    return render(
        request=request,
        template_name='cars/car_details.html',
        context={
            'car': car
        }
    )


@login_required()
def car_create(request):
    car_form = CarForm(request.POST or None)

    if car_form.is_valid():
        car_form.save()
        return redirect('cars:car_list_all')

    return render(
        request=request,
        template_name='cars/car_form.html',
        context={
            'car_form': car_form
        }
    )


@login_required()
def car_edit(request, car_id):
    car = Car.objects.get(pk=car_id)
    car_form = CarForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=car)

    if car_form.is_valid():
        car_form.save()
        return redirect('cars:car_list_all')

    return render(
        request=request,
        template_name='cars/car_form.html',
        context={
            'car_form': car_form
        }
    )


@login_required()
def car_delete(request, car_id):
    car = Car.objects.get(pk=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('cars:car_list_all')

    return render(
        request=request,
        template_name='cars/car_delete.html',
        context={
            'car': car
        }
    )


