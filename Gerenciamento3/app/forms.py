# No arquivo forms.py

from django import forms
from .models import MovimentacaoProduto

class MovimentacaoProdutoForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoProduto
        fields = ['subsector_origem', 'subsector_destino', 'quantidade_movimentada', 'transacao']
