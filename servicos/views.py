from django.shortcuts import render, redirect, get_object_or_404,redirect
from .models import *
from .form import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, "servicos/index.html")

def listar(request, servico):
    profissional = Profissional.objects.filter(servico=servico)
    itens_por_pagina = 3
    paginador = Paginator(profissional, itens_por_pagina)  
    pagina = request.GET.get('page')
    try:
        pag_obj = paginador.page(pagina)
    except PageNotAnInteger:
        pag_obj = paginador.page(1)
    except EmptyPage:
        pag_obj = paginador.page(paginador.num_pages)

    context = {'profissional': profissional, 'servico':servico, 'pag_obj': pag_obj}
    return render(request, "servicos/listar_profissionais.html",context)

def buscar_profissionais(request):
    nome = None 
    if 'q' in request.GET:
        print('entrou no if')
        termo_pesquisa = request.GET['q']
        print(termo_pesquisa)
        profissionais = Profissional.objects.buscar_por_nome(termo_pesquisa)
        nome = termo_pesquisa 
    else:
        profissionais = Profissional.objects.all()

    context = {'profissionais': profissionais, 'nome': nome}
    return render(request, 'servicos/listar_profissionais.html', context)

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
    foto = Fotos_servico.objects.filter(profissional=profissional)
    context = {'profissional': profissional, 'foto':foto}
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

def fotos_profissional(request):
    profissional = Profissional.objects.filter(nome=request.user.username).first()
    if request.method == 'POST':
        form = Fotos_servicoForm(request.POST,request.FILES)
        if form.is_valid():
            foto = form.save(commit=False)
            foto.profissional = profissional
            print(foto.profissional)
            foto.save()
            return redirect('perfil')
    else:
        form = Fotos_servicoForm()

    return render(request, "perfis/fotos_form.html", {'form': form})

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

        if i.ativo == True:
            i.ativo = 'Ativo'
        else:
            i.ativo = 'Inativo'
         
    context = {'contrato': contrato, }
    return render(request, "servicos/contratos_cliente.html", context)

def contrato_cancelar(request,id):
    contrato = get_object_or_404(Contrato, id=id)
    contrato.delete()
    return redirect('perfil') 

def contratos_profissional(request):
    profissionais = Profissional.objects.filter(nome=request.user.username).first()
    contrato = Contrato.objects.filter(profissional=profissionais, ativo=True)
    for i in contrato:
        if i.confirmado == True:
            i.confirmado = 'Confirmado'
        else:
            i.confirmado = 'Aguardando confiramção'

        if i.ativo == True:
            i.ativo = 'Ativo'
        else:
            i.ativo = 'Inativo'            
        
    context = {'contrato': contrato, }
    return render(request, "servicos/contratos_profissional.html", context)

def contrato_confirmar(request,id):
    contrato = get_object_or_404(Contrato, id=id)
    print(contrato)
    contrato.confirmado = True  
    contrato.save()
    return redirect('contratos_profissional') 

