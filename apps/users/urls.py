from django.urls import path

from . import views


urlpatterns = [
    path('confirmacao/', views.confirmacao, name='confirmacao'),
]
