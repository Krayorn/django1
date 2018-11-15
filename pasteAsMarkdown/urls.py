from django.urls import path
from . import views

app_name = 'pasteAsMarkdown'
urlpatterns = [
    path('paste/', views.PasteAsMarkdownIndex.as_view(), name='index'),
    path('create/', views.create , name='create'),
    path( 'paste/<str:markdownUrl>/', views.show, name='detail'),
]
