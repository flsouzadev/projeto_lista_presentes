from django import forms

from .models import Item, Item2

# class AusenteFormulario(forms.Form):
#     ausente = forms.CharField(
#         label='Insira seu nome para concluirmos a confirmação',
#         max_length=100,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Ex.: Ana Carolina',
#         })
#     )
    
#     ausente_rg = forms.CharField(
#         label='Insira seu Rg para nosso controle',
#         max_length=20,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Digite seu RG',
#         })
#     )


# class QtdPessoasFormulario(forms.Form):
#     qtdPessoas = forms.CharField(
#         label='Insira a quantidade de pessoas incluindo você',
#         max_length=10,
#         widget=forms.NumberInput(attrs={
#             'class': 'form-control col-sm-2',
#             'placeholder': 'Quantas pessoas?',
#             'classList': 'col',
#             'min': 0,
#             'id': 'qtdPessoas',  # Adicionando o id aqui
#             'name': 'qtdPessoas',  # Adicionando o name aqui
#         })
#     )

#     def __init__(self, *args, **kwargs):
#         super(QtdPessoasFormulario, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['id'] = field_name
#             field.widget.attrs['name'] = field_name
  
# class ListaForm(forms.Form):
    
#     AREA_DE_SERVICO_CHOICES = [
#         ('vassoura', 'Vassoura'),
#         ('rodo', 'Rodo'),
#         ('pa', 'Pá'),
#         ('pano_de_limpeza', 'Pano de Limpeza'),
#         ('escova_de_limpeza', 'Escova de Limpeza'),
#         ('pregador_de_roupa', 'Pregador de Roupa'),
#         ('varal_de_chao', 'Varal de Chão'),
#         ('balde', 'Balde'),
#     ]

#     BANHEIRO_CHOICES = [
#         ('toalha_de_banho', 'Toalha de Banho'),
#         ('toalha_de_rosto', 'Toalha de Rosto'),
#         ('toalha_de_piso', 'Toalha de Piso'),
#         ('lixeira_para_banheiro', 'Lixeira para Banheiro (Inox ou Cor Neutra)'),
#         ('escova_sanitaria', 'Escova Sanitária'),
#         ('tapetes', 'Tapetes'),
#     ]

#     QUARTO_CHOICES = [
#         ('cabides', 'Cabides'),
#         ('jogo_de_lencol', 'Jogo de Lençol (Cama Casal Padrão - 1,88 x 1,38)'),
#         ('coberta', 'Coberta'),
#         ('colcha', 'Colcha'),
#         ('fronhas', 'Fronhas'),
#     ]

#     COZINHA_CHOICES = [
#         ('espremedor_de_batata', 'Espremedor de Batata'),
#         ('potes_hermeticos', 'Potes Herméticos'),
#         ('descanso_de_panela', 'Descanso de Panela'),
#         ('copo_de_medida', 'Copo de Medida'),
#         ('assadeiras', 'Assadeiras'),
#         ('pratos', 'Pratos'),
#         ('escorredor_de_massa', 'Escorredor de Massa'),
#         ('escorredor_de_loucas', 'Escorredor de Louças (Inox ou Cor Neutra)'),
#         ('peneira_media', 'Peneira Média'),
#         ('pano_de_prato', 'Pano de Prato'),
#         ('pano_de_pia', 'Pano de Pia'),
#         ('saleiro', 'Saleiro'),
#         ('luva_termica', 'Luva Térmica'),
#         ('jogo_americano', 'Jogo Americano'),
#         ('rodinho_de_pia', 'Rodinho de Pia'),
#         ('jogo_de_talheres', 'Jogo de Talheres'),
#         ('boleira', 'Boleira'),
#         ('tabua_de_frios', 'Tábua de Frios'),
#         ('forma_de_bolo_redonda', 'Forma de Bolo Redonda'),
#     ]
    
#     OUTROS = [
#         ('outros', 'Outros'),
#     ]

#     area_de_servico = forms.MultipleChoiceField(choices=AREA_DE_SERVICO_CHOICES, widget=forms.CheckboxSelectMultiple)
#     banheiro = forms.MultipleChoiceField(choices=BANHEIRO_CHOICES, widget=forms.CheckboxSelectMultiple)
#     quarto = forms.MultipleChoiceField(choices=QUARTO_CHOICES, widget=forms.CheckboxSelectMultiple)
#     cozinha = forms.MultipleChoiceField(choices=COZINHA_CHOICES, widget=forms.CheckboxSelectMultiple)
#     outros = forms.MultipleChoiceField(choices=OUTROS, widget=forms.CheckboxSelectMultiple)
    
    
from django import forms

class FormularioLista(forms.Form):
    area_servico = forms.BooleanField(label='Área de Serviço', required=False)
    banheiro = forms.BooleanField(label='Banheiro', required=False)
    quarto = forms.BooleanField(label='Quarto', required=False)
    cozinha = forms.BooleanField(label='Cozinha', required=False)
    outros = forms.BooleanField(label='Outros', required=False)

    # Adicione mais campos conforme necessário para os itens de cada área

