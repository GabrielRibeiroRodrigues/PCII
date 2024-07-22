from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LoginView
urlpatterns = [
    
    #CRIAR NOVO PRODUTO
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto-create'),
    
    #VER A LISTA DE PRODUTOS E DETALHES
    path('produtos/', views.ProdutoListView.as_view(), name='produto-list'),
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='produto-detail'),
   
    #CRIAR NOVA MOVIMENTACAO, SELECIONANDO O SUBSETOR DE ORIGEM PRIMEIRO
    path('select_subsectors/', views.select_subsectors_movimentacoes, name='select_subsectors'),
    path('select_products/<int:origem_id>/<int:destino_id>/', views.select_products, name='select_products'),
    path('movimentacao_success/', views.movimentacao_success, name='movimentacao_success'),
    
    #VER LISTA DE MOVIMENTAÇÕES 
    path('movimentacao_list/', views.MovimentacaoListView.as_view(), name='movimentacao_list'),
    #VER LISTA DE PRODUTOS POR SETOR (Preciso  criar o filtro pra selecionar o setor ainda)   
    path('setor/<int:setor_id>/produtos/', views.ProdutosPorSetorListView.as_view(), name='produtos-por-setor'),

    #VER LISTA DE PRODUTOS POR SUBSETOR
    path('subsetor/<int:subsetor_id>/produtos/', views.ProdutosPorSubsetorListView.as_view(), name='produtos-por-subsetor'),
    
    #VER LISTA DE PRODUTOS POR FABRICANTE
    path('produtos-por-fabricante/', views.ProdutosPorFabricanteListView.as_view(), name='produtos-por-fabricante'),
    
    #VER LISTA DE PRODUTOS POR TIPO DE EMBALAGEM
    path('produtos-por-tipo-embalagem/', ProdutosPorTipoEmbalagemListView.as_view(), name='produtos-por-tipo-embalagem'),

    #VER LISTA DE PRODUTOS POR MARCA
    path('marcas/', views.ProdutosPorMarcaListView.as_view(), name='marca-list'),
   
    #VER LISTA DE PRODUTOS POR TIPO DE TRANSAÇÃO    
    path('produtos-por-transacao/', views.ProdutosPorTransacaoListView.as_view(), name='produtos-por-transacao'),
    
    #MINHA HOME
    path('', views.home, name='home'),  

    #ADICIONAR PRODUTO NO ESTOQUE
    path('adicionar_produto_estoque/<int:subsetor_id>/', adicionar_produto_estoque, name='adicionar_produto_estoque'),
    path('selecionar_subsetor_adicao/', views.selecionar_subsetor_adicao, name='selecionar_subsetor_adicao'),

    #PAGINA DE TRANSAÇÕES
    path('transacoes/', views.transacoes, name='transacoes-tipos'),

    #INFORMAÇÕES USUARIO
    path('user-subsetor/', user_subsetor_view, name='user_subsetor'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),    
]
