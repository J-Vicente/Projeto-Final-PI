from django.forms import ModelForm
from django import forms
from .models import Cliente, Profissional

ESTADOS = [('0', '--Selecione--'), ('1', 'AC'), ('2', 'AL'), ('3', 'AP'), ('4', 'AM'), 
    ('5', 'BA'), ('6', 'CE'), ('7', 'DF'), ('8', 'ES'), ('9', 'GO'), ('10', 'MA'), 
    ('11', 'MT'), ('12', 'MS'), ('13', 'MG'), ('14', 'PA'), ('15', 'PB'), ('16', 'PR'), 
    ('17', 'PE'), ('18', 'PI'), ('19', 'RJ'), ('20', 'RN'), ('21', 'RS'), ('22', 'RO'), 
    ('23', 'RR'), ('24', 'SC'), ('25', 'SP'), ('26', 'SE'), ('27', 'TO')]

SERVICOS = [('0', '--Selecione--'),('1', 'Babá'), ('2', 'Cozinheiro(a)'), ('3', 'Eletricista'), 
    ('4', 'Encanador(a)'), ('5', 'Faxina'), ('6', 'Informática'), ('7', 'Jardinagem'), 
    ('8', 'Lava-jato'), ('9', 'Pintura')]


class ClienteForm(ModelForm):

    class Meta:       
        model = Cliente
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'sobrenome' : forms.TextInput(attrs={'class': 'form-control' }),
            'email' : forms.EmailInput(attrs={'class': 'form-control' }),
            'celular' : forms.TextInput(attrs={'class': 'form-control' }),
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control' }),
            'cpf' : forms.TextInput(attrs={'class': 'form-control' }),
            'endereco' : forms.TextInput(attrs={'class': 'form-control' }),
            'cep' : forms.TextInput(attrs={'class': 'form-control' }),
            'cidade' : forms.TextInput(attrs={'class': 'form-control' }),
            'estado' : forms.Select(attrs={'class': 'form-control'}, choices=ESTADOS),
        }

class ProfissionalForm(ModelForm):

    class Meta:
        model = Profissional
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'sobrenome' : forms.TextInput(attrs={'class': 'form-control' }),
            'email' : forms.EmailInput(attrs={'class': 'form-control' }),
            'celular' : forms.TextInput(attrs={'class': 'form-control' }),
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control' }),
            'cpf' : forms.TextInput(attrs={'class': 'form-control' }),
            'endereco' : forms.TextInput(attrs={'class': 'form-control' }),
            'cep' : forms.TextInput(attrs={'class': 'form-control' }),
            'cidade' : forms.TextInput(attrs={'class': 'form-control' }),                     
            'estado' : forms.Select(attrs={'class': 'form-control'}, choices=ESTADOS),      
            'servico' : forms.Select(attrs={'class': 'form-control' }, choices=SERVICOS),
        }