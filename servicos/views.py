from django.shortcuts import render
from .models import *
from .form import ClienteForm, ProfissionalForm

# Create your views here.


def index(request):
    return render(request, "servicos/index.html")

def listar(request):
    profissional = Profissional.objects.all()
    context = {'profissional': profissional}
    return render(request, "servicos/listar_profissionais.html",context)

def perfil_profissional(request):
    return render(request, "perfis/perfil_profissional.html")

def perfil_cliente(request):
    cliente = Cliente.objects.all()
    context = {'cliente': cliente}
    return render(request, "perfis/perfil_cliente.html", context)

def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = ClienteForm()
            return redirect('perfil_cliente')
    else:
        form = ClienteForm()

    return render(request, "perfis/cliente_form.html", {'form': form})

def cadastro_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = ProfissionalForm()
            return redirect('index')
    else:
        form = ProfissionalForm()

    return render(request, "perfis/profissional_form.html", {'form': form})