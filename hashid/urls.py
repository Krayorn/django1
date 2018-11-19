from django.urls import path
from . import views

app_name = 'hashid'
urlpatterns = [
    path('', views.Hashid.as_view(), name='index'),
]
