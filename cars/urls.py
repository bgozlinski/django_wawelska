from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('', views.car_list_all, name='car_list_all'),
    path('<int:car_id>/', views.details, name='car_details'),
    path('add/', views.car_create, name='car_create'),
    path('delete/<int:car_id>/', views.car_delete, name='car_delete'),
    path('edit/<int:car_id>/', views.car_edit, name='car_edit'),


]
