from django.http import HttpResponse
from django.shortcuts import render, redirect


def cadastro(request):
    return render(request, 'users/cadastro.html')
