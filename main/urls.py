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
from servicos.views import index, listar, perfil_profissional, perfil_cliente, cadastro_cliente, cadastro_profissional
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("listar/", listar, name="listar"),
    path("perfil_profissional/", perfil_profissional, name="perfil_profissional"),
    path("perfil_cliente/", perfil_cliente, name="perfil_cliente"),
    path('cadastro_cliente/',cadastro_cliente, name='cadastro_cliente'),
    path('cadastro_profissional/', cadastro_profissional, name='cadastro_profissional'),
    path("accounts/", include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
