from django.shortcuts import render

def homeview(request):
    return render(
        request=request,
        template_name='home.html',
    )