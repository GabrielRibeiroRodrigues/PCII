from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from .forms import *
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_form.html'
    success_url = '/produtos/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['detalhe_form'] = DetalheProdutoForm(self.request.POST)
        else:
            context['detalhe_form'] = DetalheProdutoForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        detalhe_form = context['detalhe_form']
        if detalhe_form.is_valid():
            produto = form.save()
            detalhe_produto = detalhe_form.save(commit=False)
            detalhe_produto.produto = produto
            detalhe_produto.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class MovimentacaoCreateView(CreateView):
    model = MovimentacaoProduto
    form_class = MovimentacaoForm
    template_name = 'movimentacao_form.html'
    success_url = '/movimentacoes/'

class MovimentacaoListView(ListView):
    model = MovimentacaoProduto
    template_name = 'movimentacao_list.html'

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'

class ProdutosPorSetorListView(ListView):
    model = Produto
    template_name = 'produtos_por_setor.html'

    def get_queryset(self):
        # Obter o ID do setor a partir dos parâmetros da URL
        setor_id = self.kwargs['setor_id']
        
        # Filtrar produtos pelo setor específico
        return Produto.objects.filter(detalhes__subsetor__setor_id=setor_id)

class ProdutosPorSubsetorListView(ListView):
    model = DetalheProduto
    template_name = 'produtos_por_subsetor.html'
    context_object_name = 'produtos_por_subsetor'

    def get_queryset(self):
        subsetor_id = self.kwargs['subsetor_id']
        return DetalheProduto.objects.filter(subsetor_id=subsetor_id)

class ProdutosPorTipoEmbalagemListView(ListView):
    template_name = 'produtos_por_tipo_embalagem.html'
    context_object_name = 'tipos_embalagem'

    def get_queryset(self):
        tipos_embalagem = TipoEmbalagem.objects.all()
        for tipo in tipos_embalagem:
            # Obtém todos os produtos relacionados a este tipo de embalagem
            produtos = DetalheProduto.objects.filter(tipo_embalagem_produto=tipo)
            # Atribui a lista de produtos ao tipo de embalagem
            tipo.produtos_set = produtos
        return tipos_embalagem

class ProdutosPorFabricanteListView(ListView):
    template_name = 'produtos_por_fabricante.html'
    context_object_name = 'fabricantes'

    def get_queryset(self):
        fabricantes = Fabricante.objects.all()
        for fabricante in fabricantes:
            produtos = DetalheProduto.objects.filter(produto__fabricante=fabricante)
            fabricante.produtos_set = produtos
        return fabricantes    

class ProdutosPorTransacaoListView(ListView):
    template_name = 'produtos_por_transacao.html'
    context_object_name = 'transacoes'

    def get_queryset(self):
 
        transacoes = Transaction.objects.all().prefetch_related('movimentacoes')
        return transacoes