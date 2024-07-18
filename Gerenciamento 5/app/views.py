from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from .forms import *
from django.shortcuts import render
from django.urls import reverse_lazy
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

# views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import DetalheProduto, Subsector
from .forms import SubsectorSelectForm

# views.py
class ProdutosPorSubsetorListView(ListView):
    model = DetalheProduto
    template_name = 'produtos_por_subsetor.html'
    context_object_name = 'produtos_por_subsetor'

    def get_queryset(self):
        subsetor_id = self.request.GET.get('subsetor')
        if subsetor_id:
            produtos = DetalheProduto.objects.filter(subsetor_id=subsetor_id)
            return produtos
        return DetalheProduto.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SubsectorSelectForm(self.request.GET or None)
        context['form'] = form
        return context



class ProdutosPorTipoEmbalagemListView(ListView):
    model = DetalheProduto
    template_name = 'produtos_por_tipo_embalagem.html'
    context_object_name = 'produtos_por_tipo_embalagem'

    def get_queryset(self):
        tipo_embalagem_id = self.request.GET.get('tipo_embalagem')
        if tipo_embalagem_id:
            produtos = DetalheProduto.objects.filter(tipo_embalagem_produto_id=tipo_embalagem_id)
            return produtos
        return DetalheProduto.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TipoEmbalagemSelectForm(self.request.GET or None)
        context['form'] = form
        return context
class ProdutosPorFabricanteListView(ListView):
    model = DetalheProduto
    template_name = 'produtos_por_fabricante.html'
    context_object_name = 'produtos_por_fabricante'

    def get_queryset(self):
        fabricante_id = self.request.GET.get('fabricante')
        if fabricante_id:
            produtos = DetalheProduto.objects.filter(produto__fabricante_id=fabricante_id)
            return produtos
        return DetalheProduto.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = FabricanteSelectForm(self.request.GET or None)
        context['form'] = form
        return context

class ProdutosPorTransacaoListView(ListView):
    model = MovimentacaoProduto
    template_name = 'produtos_por_transacao.html'
    context_object_name = 'produtos_por_transacao'

    def get_queryset(self):
        transacao_id = self.request.GET.get('transacao')
        if transacao_id:
            movimentacoes = MovimentacaoProduto.objects.filter(transacao_id=transacao_id)
            produtos = [movimentacao.detalhe_produto for movimentacao in movimentacoes]
            return produtos
        return MovimentacaoProduto.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TransacaoSelectForm(self.request.GET or None)
        context['form'] = form
        return context

class InstituicaoListView(ListView):
    model = Instituic
    template_name = 'instituicao_list.html'
    context_object_name = 'instituicoes'

class InstituicaoCreateView(CreateView):
    model = Instituic
    template_name = 'instituicao_form.html'
    fields = ['razao_social', 'nome_fantasia', 'cnpj', 'cep']
    success_url = reverse_lazy('instituicao-list')

class InstituicaoUpdateView(UpdateView):
    model = Instituic
    template_name = 'instituicao_form.html'
    fields = ['razao_social', 'nome_fantasia', 'cnpj', 'cep']
    success_url = reverse_lazy('instituicao-list')

class InstituicaoDeleteView(DeleteView):
    model = Instituic
    template_name = 'instituicao_confirm_delete.html'
    success_url = reverse_lazy('instituicao-list')

class UnidadeInstituicaoListView(ListView):
    model = InstituicUnidade
    template_name = 'instituicaounidade_list.html'
    context_object_name = 'unidades'

class UnidadeInstituicaoCreateView(CreateView):
    model = InstituicUnidade
    template_name = 'instituicaounidade_form.html'
    fields = '__all__'
    success_url = reverse_lazy('unidade-list')

class UnidadeInstituicaoUpdateView(UpdateView):
    model = InstituicUnidade
    template_name = 'instituicaounidade_form.html'
    fields = '__all__'
    success_url = reverse_lazy('unidade-list')

class UnidadeInstituicaoDeleteView(DeleteView):
    model = InstituicUnidade
    template_name = 'instituicaounidade_confirm_delete.html'
    success_url = reverse_lazy('unidade-list')

class ProdutosPorMarcaListView(ListView):
    model = DetalheProduto
    template_name = 'produtos_por_marca.html'
    context_object_name = 'produtos_por_marca'

    def get_queryset(self):
        marca_id = self.request.GET.get('marca')
        if marca_id:
            produtos = DetalheProduto.objects.filter(produto__marca_id=marca_id)
            return produtos
        return DetalheProduto.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = MarcaSelectForm(self.request.GET or None)
        context['form'] = form
        return context

