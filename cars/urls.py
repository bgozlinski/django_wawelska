from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('all/', views.car_list_all, name='car_list_all'),
]
