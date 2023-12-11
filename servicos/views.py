from django.shortcuts import render, redirect, get_object_or_404,redirect
from .models import *
from .form import ClienteForm, ProfissionalForm
from django.contrib.auth.models import User


def perfil(request):    
    cliente = Cliente.objects.filter(nome=request.user.username).first()
    profissional = Profissional.objects.filter(nome=request.user.username).first()
    if cliente is not None:
        print(f"Usuário {request.user.username} é um cliente.")
        return redirect ('perfil_cliente')
        
    elif profissional is not None:
        print(f"Usuário {request.user.username} é um profissional.")       
        return redirect('perfil_profissional')

def index(request):
    return render(request, "servicos/index.html")

def listar(request, servico):
    profissional = Profissional.objects.filter(servico=servico)
    context = {'profissional': profissional, 'servico':servico}
    return render(request, "servicos/listar_profissionais.html",context)

def perfil_profissional(request):
    return render(request, "perfis/perfil_profissional.html")

def perfil_cliente(request):
    cliente = Cliente.objects.filter(nome=request.user.username).first()
    print(cliente.nome)
    context = {'cliente': cliente}
    return render(request, "perfis/perfil_cliente.html", context)

def editar_cliente(request,id):
    cliente = get_object_or_404(Cliente,id=id)
   
    if request.method == 'POST':
        form = ClienteForm(request.POST,request.FILES,instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('perfil_cliente')
    else:
        form = ClienteForm(instance=cliente)

    return render(request,'perfis/cliente_form.html',{'form':form})

def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = ClienteForm()
            return redirect('login')
    else:
        form = ClienteForm()

    return render(request, "perfis/cliente_form.html", {'form': form})

def cadastro_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = ProfissionalForm()
            return redirect('login')
    else:
        form = ProfissionalForm()

    return render(request, "perfis/profissional_form.html", {'form': form})