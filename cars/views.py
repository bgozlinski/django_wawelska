from django.shortcuts import render


def car_list_all(request):
    return render(
        request=request,
        template_name='cars/car_list_all.html'
    )
