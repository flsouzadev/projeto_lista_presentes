from django import forms
    
from django import forms

class FormularioLista(forms.Form):
    area_servico = forms.BooleanField(label='Área de Serviço', required=False)
    banheiro = forms.BooleanField(label='Banheiro', required=False)
    quarto = forms.BooleanField(label='Quarto', required=False)
    cozinha = forms.BooleanField(label='Cozinha', required=False)
    outros = forms.BooleanField(label='Outros', required=False)
