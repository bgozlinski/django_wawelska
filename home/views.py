from django.shortcuts import render


def home_view(request):
    return render(
        request=request,
        template_name='home/home.html',
    )

def ukaz_view(request):
    return render(
        request=request,
        template_name='home/ukaz.html'
    )
