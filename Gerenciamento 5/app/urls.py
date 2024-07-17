from django.urls import path
from . import views
from .views import ProdutosPorTipoEmbalagemListView

urlpatterns = [
    path('produtos/', views.ProdutoListView.as_view(), name='produto-list'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto-create'),
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='produto-detail'),
    path('movimentacao/nova/', views.MovimentacaoCreateView.as_view(), name='movimentacao-create'),
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
     path('marcas/', views.MarcaListView.as_view(), name='marca-list'),
    path('marcas/nova/', views.MarcaCreateView.as_view(), name='marca-create'),
    path('marcas/<int:pk>/', views.MarcaUpdateView.as_view(), name='marca-update'),
    path('marcas/<int:pk>/excluir/', views.MarcaDeleteView.as_view(), name='marca-delete'),
    path('', views.home, name='home'),
]
