from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list_all, name='car_list_all'),
]
