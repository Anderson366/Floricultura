"""floricultura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tela_inicial, name='tela_inicial'),
    path('listar_itens', views.listar_itens, name='listar_itens'),
    path('inserir_produto', views.inserir_produto, name='inserir_produto'),
    path('efetuar_venda',views.efetuar_venda, name='efetuar_venda'),
    path('realizar_venda', views.realizar_venda, name='realizar_venda'),
    path('lista_produtos', views.cadastro_produto, name='lista_produtos'),
    path('salvar_produto', views.salvar_produto, name='salvar_produto'),
    path('lista_clientes', views.lista_clientes, name='lista_clientes'),
    path('salva_cliente', views.salvar_cliente, name='salva_clientes'),
]
