     
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movimentacoes/', views.lista_movimentacoes, name='lista_movimentacoes'),
    path('movimentacoes/criar/', views.criar_movimentacao, name='criar_movimentacao'),
]
