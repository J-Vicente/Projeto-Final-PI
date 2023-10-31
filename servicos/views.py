from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "servicos/index.html")

def listar(request):
    return render(request, "servicos/listar_profissionais.html")

def perfil_profissional(request):
    return render(request, "perfis/perfil_profissional.html")

def perfil_cliente(request):
    return render(request, "perfis/perfil_cliente.html")

def cadastro_cliente(request):
    return render(request, "perfis/cliente_form.html")

def cadastro_profissional(request):
    return render(request, "perfis/profissional_form.html")