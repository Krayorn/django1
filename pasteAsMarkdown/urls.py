from django.urls import path
from . import views

app_name = 'pasteAsMarkdown'
urlpatterns = [
    path('', views.PasteAsMarkdownIndex.as_view(), name='index'),
    path( '<str:markdownUrl>/', views.show, name='detail'),
]
