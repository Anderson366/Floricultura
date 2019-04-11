from django.forms import ModelForm

from .models import Cliente, Produto, Venda, Itens

class ClienteForm(ModelForm):
    class Meta:
         model = Cliente
         fields = '__all__'

class ProdutoForm(ModelForm):
    class Meta:
         model = Produto
         fields = '__all__'

class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'

class ItensForm(ModelForm):
    class Meta:
        model = Itens
        fields = '__all__'