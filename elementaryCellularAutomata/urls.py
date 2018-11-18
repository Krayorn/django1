from django.urls import path
from . import views

app_name = 'elementaryCellularAutomata'
urlpatterns = [
    path('', views.ElementaryCellularAutomata.as_view(), name='index'),
]
