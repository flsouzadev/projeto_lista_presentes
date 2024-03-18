import sqlite3
from django.shortcuts import render, redirect
from apps.users.models import Convidado
from django.contrib.messages import constants
from django.contrib import messages

def confirmacao(request):
    if request.method == 'GET':
        return render(request, 'users/confirmacao.html')

    elif request.method == 'POST':
        nome_ausente = request.POST.get('nomeAusente')

        if nome_ausente != '':
            # Lógica para tratamento dos campos nomeAusente, rgAusente
            rg_ausente = request.POST.get('rgAusente')
            presente = request.POST.get('presente')

            if rg_ausente:
                presenca = False
            else:
                presenca = True


            if Convidado.objects.filter(rg=rg_ausente).exists():
                messages.add_message(request, constants.ERROR, f"{nome_ausente}, você já confirmou presença!")
                return redirect('confirmacao')
            else:
                convidado = Convidado(nome=nome_ausente, rg=rg_ausente, presente=presente, presenca=presenca)
                convidado.save()  # Salvando no banco de dados
                messages.add_message(request, constants.SUCCESS, f"{nome_ausente}, sua confirmação foi realizada com sucesso!")

            return redirect('confirmacao')

        else:
            # Lógica para tratamento dos campos nomePresente, rgPresente
            nome_presente = request.POST.get('nomePresente')
            rg_presente = request.POST.get('rgPresente')

            # Acessando os valores dos checkboxes
            area_servico = request.POST.getlist('area_servico[]')
            banheiro = request.POST.getlist('banheiro[]')
            quarto = request.POST.getlist('quarto[]')
            cozinha = request.POST.getlist('cozinha[]')
            outros = request.POST.getlist('outros')

            all_values_list = area_servico + banheiro + quarto + cozinha + outros

            if Convidado.objects.filter(rg=rg_presente).exists():
                messages.add_message(request, constants.ERROR, f"{nome_presente}, você já confirmou presença!")
                return redirect('confirmacao')
            
                        # Consulta para obter todos os presentes(brindes)
            qtd_presentes = Convidado.objects.exclude(presente=None)
            array_presentes=[]
            # Iterando sobre os convidados presentes e imprimindo seus nomes
            for cada_presente in qtd_presentes:
                array_presentes.append(cada_presente)
                
                dados= [array_presentes for array_presentes in all_values_list]
                # for array_presentes in all_values_list:
                print(dados)
                    
                return render(request, 'users/confirmacao.html', {"cada_presente": dados})

            if 'outros' in all_values_list:
                if len(all_values_list) == 1:
                    messages.add_message(request, constants.WARNING, f"{nome_presente}, por favor, por ter selecionado o item 'outros' entre em contato com a noiva para informar o que deseja dar de presente.")
                    return redirect('confirmacao')
                else:
                    messages.add_message(request, constants.WARNING, f"{nome_presente}, por favor, por ter selecionado o item 'outros' entre em contato com a noiva para informar o que deseja dar de presente.")

            if rg_presente and nome_presente and any(all_values_list):  # Verifica se todos os campos estão preenchidos
                presenca = True
                # Convertendo a lista de valores selecionados em uma string separada por vírgula
                valores_selecionados = ",".join(all_values_list)
                # Salvando no banco de dados
                convidado = Convidado(nome=nome_presente, rg=rg_presente, presente=valores_selecionados, presenca=presenca)
                convidado.save()  # Salvando no banco de dados

                messages.add_message(request, constants.SUCCESS, f"{nome_presente}, sua confirmação foi realizada com sucesso!")
                
            else:
                messages.add_message(request, constants.ERROR, f"Preencha todos os campos obrigatórios!")

            return redirect('confirmacao')
