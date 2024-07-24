from django.shortcuts import *
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
@login_required
def home(request):
    return render(request, 'home.html')
#CRIANDO PRODUTOS
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
#LISTA DE PRODUTOS
class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        user = self.request.user
        subsetor = user.subsetor
        if subsetor:
            return Produto.objects.filter(detalhes__subsetor=subsetor).distinct()
        return Produto.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        subsetor = user.subsetor
        context['user'] = user
        context['subsetor'] = subsetor
        return context
#DETALHES DO PRODUTO
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'

#LISTA DE MOVIMENTAÇÕES
class MovimentacaoListView(ListView):
    model = MovimentacaoProduto
    template_name = 'movimentacao_list.html'
#FUNCÃO PARA SELECIONAR SUB SETORES PARA MOVIMENTACAO DE PRODUTOS
@login_required
def select_subsectors_movimentacoes(request):
    user = request.user
    subsetor_origem = user.subsetor if user.subsetor else None
    
    if request.method == "POST":
        form = SubsectorSelecttForm(request.POST)
        if form.is_valid():
            subsector_origem = form.cleaned_data['subsetor_origem']
            subsector_destino = form.cleaned_data['subsetor_destino']
            return redirect('select_products', origem_id=subsector_origem.id, destino_id=subsector_destino.id)
    else:
        initial_data = {'subsetor_origem': subsetor_origem}
        form = SubsectorSelecttForm(initial=initial_data)
    
    return render(request, 'select_subsectors.html', {'form': form})
#FUNCÃO PARA SELECIONAR PRODUTOS DEPEDENDO DO SUBSETOR 
def select_products(request, origem_id, destino_id):
    subsector_origem = get_object_or_404(Subsector, id=origem_id)
    subsector_destino = get_object_or_404(Subsector, id=destino_id)
    produtos_disponiveis = DetalheProduto.objects.filter(subsetor=subsector_origem)

    if request.method == "POST":
        form = MovimentacaoForm_Completo(request.POST, subsetor_origem=subsector_origem)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.subsector_origem = subsector_origem
            movimentacao.subsector_destino = subsector_destino
            movimentacao.save()
            return redirect('movimentacao_success')
    else:
        form = MovimentacaoForm_Completo(subsetor_origem=subsector_origem)

    return render(request, 'select_products.html', {
        'form': form,
        'produtos_disponiveis': produtos_disponiveis,
        'subsector_origem': subsector_origem,
        'subsector_destino': subsector_destino
    })      
#CRIANDO MOVIMENTAÇÕES DE PRODUTO
class MovimentacaoCreateView(CreateView):
    model = MovimentacaoProduto
    form_class = MovimentacaoForm_Completo
    template_name = 'movimentacao_form.html'
    success_url = '/movimentacoes/'



#LISTA DE PRODUTOS POR SETOR
class ProdutosPorSetorListView(LoginRequiredMixin, ListView):
    model = DetalheProduto
    template_name = 'produtos_por_setor.html'
    context_object_name = 'produtos_por_setor'

    def get_queryset(self):
        user = self.request.user
        setor = user.subsetor.setor if user.subsetor else None
        if setor:
            return DetalheProduto.objects.filter(subsetor__setor=setor)
        return DetalheProduto.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setor'] = self.request.user.subsetor.setor if self.request.user.subsetor else None
        return context

#LISTA DE PRODUTOS POR SUB SETOR

class ProdutosPorSubsetorListView(LoginRequiredMixin, ListView):
    model = DetalheProduto
    template_name = 'produtos_por_subsetor.html'
    context_object_name = 'produtos_por_subsetor'

    def get_queryset(self):
        user = self.request.user
        subsetor = user.subsetor
        if subsetor:
            return DetalheProduto.objects.filter(subsetor=subsetor)
        return DetalheProduto.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SubsectorSelectForm(self.request.GET or None)
        context['form'] = form
        context['subsetor'] = self.request.user.subsetor  
        return context
#LISTAS DE PRODUTOS FILTRADOS POR EMBALAGEM 
class ProdutosPorTipoEmbalagemListView(ListView):
    model = DetalheProduto
    template_name = 'produtos_por_tipo_embalagem.html'
    context_object_name = 'produtos_por_tipo_embalagem'

    def get_queryset(self):
        tipo_embalagem_id = self.request.GET.get('tipo_embalagem')
        user_subsector = self.request.user.subsetor
        
        if tipo_embalagem_id and user_subsector:
            return DetalheProduto.objects.filter(
                tipo_embalagem_produto_id=tipo_embalagem_id,
                subsetor=user_subsector
            )
        return DetalheProduto.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TipoEmbalagemSelectForm(self.request.GET or None)
        context['form'] = form
        return context
#LISTAS DE PRODUTOS FILTRADOS POR FABRICANTE
class ProdutosPorFabricanteListView(ListView):
    model = DetalheProduto
    template_name = 'produtos_por_fabricante.html'
    context_object_name = 'produtos_por_fabricante'

    def get_queryset(self):
        fabricante_id = self.request.GET.get('fabricante')
        user_subsector = self.request.user.subsetor

        if fabricante_id and user_subsector:
            return DetalheProduto.objects.filter(
                produto__fabricante_id=fabricante_id,
                subsetor=user_subsector
            )
        return DetalheProduto.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = FabricanteSelectForm(self.request.GET or None)
        context['form'] = form
        return context
#LISTAS DE PRODUTOS FILTRADOS POR TIPO DE TRANSAÇÃO
class ProdutosPorTransacaoListView(ListView):
    model = DetalheProduto
    template_name = 'produtos_por_transacao.html'
    context_object_name = 'produtos_por_transacao'

    def get_queryset(self):
        transacao_id = self.request.GET.get('transacao')
        user_subsector = self.request.user.subsetor

        if transacao_id and user_subsector:
            movimentacoes = MovimentacaoProduto.objects.filter(
                transacao_id=transacao_id,
                subsector_origem=user_subsector
            )
            return DetalheProduto.objects.filter(id__in=[movimentacao.detalhe_produto.id for movimentacao in movimentacoes])
        return DetalheProduto.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TransacaoSelectForm(self.request.GET or None)
        context['form'] = form
        return context

#LISTAS DE PRODUTOS FILTRADOS POR MARCA
class ProdutosPorMarcaListView(ListView):
    model = DetalheProduto
    template_name = 'produtos_por_marca.html'
    context_object_name = 'produtos_por_marca'

    def get_queryset(self):
        marca_id = self.request.GET.get('marca')
        if marca_id:
            return DetalheProduto.objects.filter(produto__marca_id=marca_id)
        return DetalheProduto.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = MarcaSelectForm(self.request.GET or None)
        context['form'] = form
        return context


#FUNÇÃO PARA CONFIRMAÇÃO DE MOVIMENTACAO
def movimentacao_success(request):
    return render(request, 'movimentacao_success.html')

#FUNÇÃO PARA PAGINA DE TRANSAÇÕES
def transacoes(request):
    return render(request, 'transacoes.html')


#SELECIONAR SUB SETOR PARA ADICIONAR NO ESTOQUE
def selecionar_subsetor_adicao(request):
    if request.method == "POST":
        form = SubsectorSelecttForm(request.POST)
        if form.is_valid():
            subsetor_origem = form.cleaned_data['subsetor_origem']
            return redirect('adicionar_produto_estoque', subsetor_id=subsetor_origem.id)
    else:
        form = SubsectorSelecttForm()
    return render(request, 'selecionar_subsetor_adicao.html', {'form': form})


#ADICIONAR PRODUTO NO ESTOQUE
def adicionar_produto_estoque(request, subsetor_id):
    subsetor_origem = get_object_or_404(Subsector, id=subsetor_id)
    subsetor_destino = subsetor_origem  # O destino é o mesmo subsetor para adição ao estoque
    produtos_disponiveis = DetalheProduto.objects.filter(subsetor=subsetor_origem)
    
    if request.method == "POST":
        form = MovimentacaoForm_Completo(request.POST, subsetor_origem=subsetor_origem, subsetor_destino=subsetor_destino)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.subsector_origem = subsetor_origem
            movimentacao.subsector_destino = subsetor_destino
            movimentacao.save()
            return redirect('movimentacao_success')
    else:
        form = MovimentacaoForm_Completo(subsetor_origem=subsetor_origem, subsetor_destino=subsetor_destino)
    
    return render(request, 'selecionar_subsetor_adicao.html', {
        'form': form,
        'produtos_disponiveis': produtos_disponiveis,
        'subsetor': subsetor_origem
    })


    return render(request, 'selecionar_subsetor_adicao.html', {
        'form': form,
        'produtos_disponiveis': produtos_disponiveis,
        'subsetor': subsetor_origem
    })
#TESTE DE USUARIO LOGADO
def user_subsetor_view(request):
    user = request.user
    subsetor = user.subsetor if hasattr(user, 'subsetor') else None
    preferred_name = user.profile_user.preferred_name if hasattr(user, 'profile_user') else None
    return render(request, 'user_subsetor.html', {'user': user, 'subsetor': subsetor, 'preferred_name': preferred_name})


    
    
