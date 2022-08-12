from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('ukaz/', views.ukaz_view, name='ukaz_view'),
]