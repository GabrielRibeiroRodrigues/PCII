from django import forms
from .models import *

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
class SubsectorSelectForm(forms.Form):
    subsetor = forms.ModelChoiceField(queryset=Subsector.objects.all(), label="Selecionar Subsetor")


class TipoEmbalagemSelectForm(forms.Form):
    tipo_embalagem = forms.ModelChoiceField(queryset=TipoEmbalagem.objects.all(), label='Tipo de Embalagem', required=True)

class FabricanteSelectForm(forms.Form):
    fabricante = forms.ModelChoiceField(queryset=Fabricante.objects.all(), label='Fabricante', required=True)

class MarcaSelectForm(forms.Form):
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), label='Marca', required=True)

class TransacaoSelectForm(forms.Form):
    transacao = forms.ModelChoiceField(queryset=Transaction.objects.all(), required=False, label='Selecione a Transação')

class SubsectorSelecttForm(forms.Form):
    subsetor_origem = forms.ModelChoiceField(queryset=Subsector.objects.all(), label="Subsetor de Origem")
    subsetor_destino = forms.ModelChoiceField(queryset=Subsector.objects.all(), label="Subsetor de Destino")

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoProduto
        fields = ['detalhe_produto', 'quantidade_movimentada', 'transacao']

    def __init__(self, *args, **kwargs):
        subsetor_origem = kwargs.pop('subsetor_origem', None)
        super(MovimentacaoForm, self).__init__(*args, **kwargs)
        if subsetor_origem:
            self.fields['detalhe_produto'].queryset = DetalheProduto.objects.filter(subsetor=subsetor_origem)

class InstituicaoSelectForm(forms.Form):
    instituicao = forms.ModelChoiceField(queryset=Instituic.objects.all(), label="Selecionar Instituição")
class AdicionarEstoqueForm(forms.ModelForm):
    quantidade_adicionar = forms.IntegerField(label='Quantidade a adicionar', min_value=1)

    class Meta:
        model = DetalheProduto
        fields = ['quantidade_adicionar']


