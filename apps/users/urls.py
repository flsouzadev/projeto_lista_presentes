from django.urls import path

from . import views

from django.views.generic import RedirectView


urlpatterns = [
    path('confirmacao/', views.confirmacao, name='confirmacao'),
    path('', RedirectView.as_view(url='/confirmacao/', permanent=True)),
]
