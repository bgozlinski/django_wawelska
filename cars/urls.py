from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    # all cars list
    path('', views.car_list_all, name='car_list_all'),
    # details of car
    path('<int:car_id>/', views.details, name='car_details'),
]
