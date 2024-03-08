from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('presente/', views.presente, name='presente'),
    path('ausente/', views.ausente, name='ausente'),
    path('listaForm/', views.listaForm, name='listaForm'),
    
]
