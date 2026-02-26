from django.urls import path
from . import views

urlpatterns = [
    path('', views.length, name='length-converter'),
    path('weight', views.weight, name='weight-converter'),
    path('temperature', views.temp, name='temperature-converter')
]