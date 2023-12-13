"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from servicos.views import *
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("listar/<str:servico>/", listar, name="listar"),
    path('buscar_profissionais/', buscar_profissionais, name='buscar_profissionais'),
    path("perfil/cliente/", perfil_cliente, name="perfil_cliente"),
    path('cadastro/cliente/',cadastro_cliente, name='cadastro_cliente'),
    path('perfil/cliente/editar/<int:id>/',editar_cliente, name='editar_cliente'),
    path("perfil/profissional/", perfil_profissional, name="perfil_profissional"),
    path('cadastro/profissional/', cadastro_profissional, name='cadastro_profissional'),
    path('perfil/profissional/editar/<int:id>/',editar_profissional, name='editar_profissional'),
    path('perfil/imagens/', fotos_profissional, name='fotos_profissional'),
    path('perfil/', perfil, name='perfil'),
    path('contrato/<int:id>/', contrato, name='contrato'),
    path('contrato/cancelar/<int:id>/', contrato_cancelar, name='contrato_cancelar'),
    path('contrato/cliente/meuscontratos/', contratos_clientes, name='contratos_clientes'),
    path('contrato/confirmar/<int:id>/', contrato_confirmar, name='contrato_confirmar'),
    path('contrato/profissional/meuscontratos/', contratos_profissional, name='contratos_profissional'),
    path("accounts/", include("django.contrib.auth.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
