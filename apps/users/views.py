from django.http import HttpResponse

from django.shortcuts import render, redirect

from .forms import AusenteFormulario, PresenteFormulario, QtdPessoasFormulario, ListaForm

from django.contrib import messages


def index(request):
    # if request.method == 'post':
    if request.method == 'POST':
        presenca = request.POST.get('presenca')
        if presenca == 'sim':
            # Redirecionar para a página de confirmação de presença
            return redirect('presente')
        elif presenca == 'nao':
            # Redirecionar para a página de ausência
            return redirect('ausente')

    # Renderizar o template do formulário
    return render(request, 'users/index.html')
    
def presente(request):
    if request.method == 'POST':
        form = QtdPessoasFormulario(request.POST)
        if form.is_valid():
            
            #encaminhar os dados para o banco de dados
            
            return redirect('listaForm')
    else:
        form = QtdPessoasFormulario()    
    return render(request, 'users/presente.html', {'form': form})


def ausente(request):
    if request.method == 'POST':
        form = AusenteFormulario(request.POST)
        if form.is_valid():
            
            #encaminhar os dados ao banco de dados
            
            meu_dado = form.cleaned_data['ausente']
            return render(request, 'users/ausente.html', {'meu_dado': meu_dado})
    else:
        form = AusenteFormulario()
    return render(request, 'users/ausente.html', {'form': form})
    

from django.shortcuts import render


def listaForm(request):
    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário aqui
            pass  # Fazer algo com os dados
    else:
        form = ListaForm()
    return render(request, 'users/listaForm.html', {'form': form})


# from django.http import HttpResponse
# from django.shortcuts import render, redirect

# from apps.users.forms import DadosForm


# def index(request):
#     # Se o método de solicitação for POST, significa que o formulário foi enviado
#     if request.method == 'POST':
#         form = DadosForm(request.POST)
#         # Verifica se o formulário é válido
#         if form.is_valid():
#             # Processa os dados do formulário aqui, se necessário
#             # Redireciona para outra página, ou exibe uma mensagem de sucesso, etc.
#             return redirect('outra_pagina')
#     else:
#         # Se o método de solicitação não for POST, exibe o formulário vazio
#         form = DadosForm()
    
#     return render(request, 'users/index.html', {'form': form})
