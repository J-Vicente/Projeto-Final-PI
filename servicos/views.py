from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'servicos/index.html')

def listar(request):
    return render(request, 'servicos/listar_profissionais.html')
