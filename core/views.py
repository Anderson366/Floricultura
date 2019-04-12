from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms  import  ClienteForm, ProdutoForm, VendaForm, ItensForm
from .models import Cliente, Produto, Venda, Itens

def tela_inicial(request):
    return render(
        request,
        'Tela_Inicial.html'
    )


def lista_clientes(request):
    clientes = Cliente.objects.all()
    form = ClienteForm
    data = {'clientes': clientes, 'form':form}
    return render(
        request,
        'Lista_Clientes.html',
        data
    )

def salvar_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_clientes')

def cadastro_produto(request):
    produtos = Produto.objects.all()
    form = ProdutoForm
    data = {'produtos': produtos, 'form': form}
    return render(
        request,
        'cadastro_produto.html',
        data
    )

def salvar_produto(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_produtos')


def efetuar_venda(request):
    vendas = Venda.objects.all()
    form = VendaForm
    data = {'vendas': vendas, 'form':form}

    return render(
        request,
        'Efetuar_Venda.html',
        data
    )
def realizar_venda(request):
    form = VendaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_itens')
    else:

        return redirect('efetuar_venda')

def listar_itens(request):
    ItensV = Itens.objects.all()
    form = ItensForm
    data = {'ItensV': ItensV, 'form': form}

    return render(
        request,
        'Lista_Itens.html',
        data
    )
def inserir_produto(request):
    form = ItensForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_itens')
    else:
        return redirect('tela_inicial')