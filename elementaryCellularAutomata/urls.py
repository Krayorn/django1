from django.urls import path
from . import views

app_name = 'elementaryCellularAutomata'
urlpatterns = [
    path('getRule/', views.ElementaryCellularAutomata.as_view(), name='index'),
    path('show/', views.show, name='show'),
]
