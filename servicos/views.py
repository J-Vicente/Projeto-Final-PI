from django.shortcuts import render, redirect, get_object_or_404,redirect
from .models import *
from .form import *
from django.contrib.auth.models import User

def index(request):
    return render(request, "servicos/index.html")

def listar(request, servico):
    profissional = Profissional.objects.filter(servico=servico)
    context = {'profissional': profissional, 'servico':servico}
    return render(request, "servicos/listar_profissionais.html",context)

# -----------------------------------------------------------------------------------------------------

def perfil(request):    
    cliente = Cliente.objects.filter(nome=request.user.username).first()
    profissional = Profissional.objects.filter(nome=request.user.username).first()
    if cliente is not None:
        print(f"Usuário {request.user.username} é um cliente.")
        return redirect ('perfil_cliente')
        
    elif profissional is not None:
        print(f"Usuário {request.user.username} é um profissional.")       
        return redirect('perfil_profissional')

def perfil_profissional(request):
    profissional = Profissional.objects.filter(nome=request.user.username).first()
    print(profissional.nome)
    context = {'profissional': profissional}
    return render(request, "perfis/perfil_profissional.html", context)

def perfil_cliente(request):
    cliente = Cliente.objects.filter(nome=request.user.username).first()
    print(cliente.nome)
    context = {'cliente': cliente}
    return render(request, "perfis/perfil_cliente.html", context)

# -----------------------------------------------------------------------------------------------------    

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

# -----------------------------------------------------------------------------------------------------

def editar_profissional(request,id):
    profissional = get_object_or_404(profissional,id=id)
   
    if request.method == 'POST':
        form = ProfissionalForm(request.POST,request.FILES,instance=profissional)
        if form.is_valid():
            form.save()
            return redirect('perfil_profissional')
    else:
        form = ProfissionalForm(instance=profissional)

    return render(request,'perfis/profissional_form.html',{'form':form})

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

# --------------------------------------------------------------------------------------------------------

def contrato(request,id):
    profissional = get_object_or_404(Profissional,id=id)
    cliente = Cliente.objects.filter(nome=request.user.username).first()
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            contrato = form.save(commit=False)
            contrato.servico = profissional.servico
            contrato.profissional = profissional
            contrato.cliente = cliente
            contrato.save()
            return redirect('perfil')
    else:
        form = ContratoForm()

    context = {'cliente': cliente, 'profissional': profissional, 'form': form}
    return render(request, "servicos/contratar.html", context)

def contratos_clientes(request):
    cliente = Cliente.objects.filter(nome=request.user.username).first()
    contrato = Contrato.objects.filter(cliente=cliente)
    for i in contrato:
        if i.confirmado == True:
            i.confirmado = 'Confirmado'
        else:
            i.confirmado = 'Aguardando confiramção'
         
    context = {'contrato': contrato, }
    return render(request, "servicos/contratos_cliente.html", context)

def contrato_cancelar(request,id):
    contrato = get_object_or_404(Contrato, id=id)
    contrato.delete()
    return redirect('contrato_clientes') 

def contratos_profissional(request):
    profissionais = Profissional.objects.filter(nome=request.user.username).first()
    contrato = Contrato.objects.filter(profissional=profissionais, ativo=True)
    for i in contrato:
        if i.confirmado == True:
            i.confirmado = 'Confirmado'
        else:
            i.confirmado = 'Aguardando confiramção'
        
    context = {'contrato': contrato, }
    return render(request, "servicos/contratos_profissional.html", context)

def contrato_confirmar(request,id):
    contrato = get_object_or_404(Contrato, id=id)
    print(contrato)
    contrato.confirmado = True  
    contrato.save()
    return redirect('contratos_profissional') 

