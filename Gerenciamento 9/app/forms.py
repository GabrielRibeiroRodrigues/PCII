from django import forms
from .models import *

#FORMULARIO PARA CRIAR PRODUTOS
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'marca', 'modelo', 'fabricante']

#FORMULARIO PARA ADICIONAR DETALHES AO PRODUTO
class DetalheProdutoForm(forms.ModelForm):
    class Meta:
        model = DetalheProduto
        fields = ['unidade_produto', 'cor_produto', 'sabor_produto', 'quantidade_embalagem_produto', 'tipo_embalagem_produto', 'quantidade_produto', 'preco_custo_produto', 'preco_venda_produto', 'subsetor']

#FORMULARIO PARA CRIAR MOVIMENTACOEES
class MovimentacaoForm_Completo(forms.ModelForm):
    class Meta:
        model = MovimentacaoProduto
        fields = ['data_hora_movimentacao', 'detalhe_produto', 'quantidade_movimentada', 'transacao']
        widgets = {
            'data_hora_movimentacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'quantidade_movimentada': forms.NumberInput(attrs={'min': 1}),
        }

    def __init__(self, *args, **kwargs):
        subsetor_origem = kwargs.pop('subsetor_origem', None)
        super(MovimentacaoForm_Completo, self).__init__(*args, **kwargs)
        if subsetor_origem:
            self.fields['detalhe_produto'].queryset = DetalheProduto.objects.filter(subsetor=subsetor_origem)
        else:
            self.fields['detalhe_produto'].queryset = DetalheProduto.objects.none()
#FORMULARIO PARA LISTA DE PRODUTOS POR SUB SETOR
class SubsectorSelectForm(forms.Form):
    subsetor = forms.ModelChoiceField(queryset=Subsector.objects.all(), label="Selecionar Subsetor")

#FORMULARIO PARA LISTA DE PRODUTOS POR SETOR
class sectorSelectForm(forms.Form):
            setor = forms.ModelChoiceField(queryset=Sector.objects.all(), label="Selecionar setor")

#FORMULARIO PARA LISTA DE PRODUTOS POR EMBALAGEM
class TipoEmbalagemSelectForm(forms.Form):
    tipo_embalagem = forms.ModelChoiceField(queryset=TipoEmbalagem.objects.all(), label='Tipo de Embalagem', required=True)

#FORMULARIO PARA LISTA DE PRODUTOS POR FABRICANTE
class FabricanteSelectForm(forms.Form):
    fabricante = forms.ModelChoiceField(queryset=Fabricante.objects.all(), label='Fabricante', required=False)

#FORMULARIO PARA LISTA DE PRODUTOS POR MARCA
class MarcaSelectForm(forms.Form):
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), label='Marca', required=True)

#FORMULARIO PARA LISTA DE PRODUTOS POR TIPO DE TRANSACAO
class TransacaoSelectForm(forms.Form):
    transacao = forms.ModelChoiceField(queryset=Transaction.objects.all(), required=False, label='Selecione a Transação')

#FORMULARIO PARA PARA SELECIONAR SUB SETORES PARA MOVIMENTACAO DE PRODUTOS
class SubsectorSelecttForm(forms.Form):
    subsetor_origem = forms.ModelChoiceField(queryset=Subsector.objects.all(), label="Subsetor de Origem")
    subsetor_destino = forms.ModelChoiceField(queryset=Subsector.objects.all(), label="Subsetor de Destino")


#FORMULARIO PARA SELECIONAR INSTITUIÇÃO
class InstituicaoSelectForm(forms.Form):
    instituicao = forms.ModelChoiceField(queryset=Instituic.objects.all(), label="Selecionar Instituição")



