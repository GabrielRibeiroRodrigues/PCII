from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import MovimentacaoProdutoForm

def lista_movimentacoes(request):
    movimentacoes = MovimentacaoProduto.objects.all()
    return render(request, 'lista_movimentacoes.html', {'movimentacoes': movimentacoes})

from django.shortcuts import render, redirect
from .models import Subsector, DetalheProduto
from .forms import MovimentacaoProdutoForm

def criar_movimentacao(request):
    subsetores = Subsector.objects.all()
    detalhes_produto = DetalheProduto.objects.all()
    
    tipos_transacao = [
        'Doação',
        'Perda',
        'Transferência',
        'Entrada',
        'Saída',
    ]

    if request.method == 'POST':
        form = MovimentacaoProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_movimentacoes')
    else:
        form = MovimentacaoProdutoForm()
    
    context = {
        'form': form,
        'subsetores': subsetores,
        'detalhes_produto': detalhes_produto,
        'tipos_transacao': tipos_transacao,
    }
    return render(request, 'criar_movimentacao.html', context)
