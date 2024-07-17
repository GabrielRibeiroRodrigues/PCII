from django import forms
from .models import Produto
from .models import MovimentacaoProduto , DetalheProduto
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'marca', 'modelo', 'fabricante']


class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoProduto
        fields = ['data_hora_movimentacao', 'subsector_origem', 'subsector_destino', 'detalhe_produto', 'quantidade_movimentada', 'transacao']



class DetalheProdutoForm(forms.ModelForm):
    class Meta:
        model = DetalheProduto
        fields = ['unidade_produto', 'cor_produto', 'sabor_produto', 'quantidade_embalagem_produto', 'tipo_embalagem_produto', 'quantidade_produto', 'preco_custo_produto', 'preco_venda_produto', 'subsetor']
