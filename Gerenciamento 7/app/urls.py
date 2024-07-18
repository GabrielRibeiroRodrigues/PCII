from django.urls import path
from . import views
from .views import ProdutosPorTipoEmbalagemListView

urlpatterns = [
    path('produtos/', views.ProdutoListView.as_view(), name='produto-list'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto-create'),
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='produto-detail'),
    path('movimentacoes/', views.MovimentacaoListView.as_view(), name='movimentacao-list'),
    path('setor/<int:setor_id>/produtos/', views.ProdutosPorSetorListView.as_view(), name='produtos-por-setor'),
    path('subsetor/<int:subsetor_id>/produtos/', views.ProdutosPorSubsetorListView.as_view(), name='produtos-por-subsetor'),
    path('produtos-por-tipo-embalagem/', ProdutosPorTipoEmbalagemListView.as_view(), name='produtos-por-tipo-embalagem'),
    path('produtos-por-fabricante/', views.ProdutosPorFabricanteListView.as_view(), name='produtos-por-fabricante'),
    path('produtos-por-transacao/', views.ProdutosPorTransacaoListView.as_view(), name='produtos-por-transacao'),
    path('instituicoes/', views.InstituicaoListView.as_view(), name='instituicao-list'),
    path('instituicoes/nova/', views.InstituicaoCreateView.as_view(), name='instituicao-create'),
    path('instituicoes/<int:pk>/editar/', views.InstituicaoUpdateView.as_view(), name='instituicao-update'),
    path('instituicoes/<int:pk>/excluir/', views.InstituicaoDeleteView.as_view(), name='instituicao-delete'),
    path('unidades/', views.UnidadeInstituicaoListView.as_view(), name='unidade-list'),
    path('unidades/nova/', views.UnidadeInstituicaoCreateView.as_view(), name='unidade-create'),
    path('unidades/<int:pk>/', views.UnidadeInstituicaoUpdateView.as_view(), name='unidade-update'),
    path('unidades/<int:pk>/excluir/', views.UnidadeInstituicaoDeleteView.as_view(), name='unidade-delete'),
    path('marcas/', views.ProdutosPorMarcaListView.as_view(), name='marca-list'),
    path('select_subsectors/', views.select_subsectors, name='select_subsectors'),
    path('select_products/<int:origem_id>/<int:destino_id>/', views.select_products, name='select_products'),
    path('movimentacao_success/', views.movimentacao_success, name='movimentacao_success'),
    path('instituicao_list/', views.filter_instituicao, name='instituicao_list'),
    path('selecionar-transacao/', views.selecionar_transacao, name='selecionar_transacao'),
    path('selecionar-subsectores/<int:transacao_id>/', views.select_subsectors, name='selecionar_subsectores'),
    path('', views.home, name='home'),
]
