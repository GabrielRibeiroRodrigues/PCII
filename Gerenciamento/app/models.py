from django.db import models
#Gerencia instituicao

class Instituic(models.Model):
    razao_social = models.CharField(max_length = 15)
    nome_fantasia = models.CharField(max_length = 15)
    cnpj = models.IntegerField()
    cep = models.IntegerField()
## Gerenciar unidade da instituicao
class InstituicUnidade(models.Model):
    id_instituic = models.ForeignKey(Instituic, related_name = 'instituic',on_delete = models.CASCADE)
    razao_social = models.CharField(max_length = 15)
    nome_fantasia = models.CharField(max_length = 15)
    cnpj = models.IntegerField()
    cep = models.IntegerField()

##Gerenciar Super setores, setores e subsetores 
class SectorSuper(models.Model):
    nome_super_setor = models.CharField(max_length = 10)
class Sector(models.Model):
    id_SS = models.ForeignKey(SectorSuper, related_name = 'nome_super_setor', on_delete = models.CASCADE)
    nome_setor = models.CharField(max_length = 10)
class Subsector(models.Model):
    id_SS = models.ForeignKey(SectorSuper, related_name = 'nome_super_setor', on_delete = models.CASCADE)
    id_S = models.ForeignKey(Sector, related_name = 'nome_setor', on_delete = models.CASCADE)
    nome_sub_setor = models.CharField(max_length = 10)

## Gerenciar categorias/grupos
class categorias(models.Model):
    nome_categoria = models.CharField(max_length = 20)
class sub_categorias(models.Model):
    id_categoria = models.ForeignKey(categorias, related_name = 'nome_categoria', on_delete = models.CASCADE)
    nome_subcategoria = models.CharField(max_length = 20)

##Transações
class Transactions(models.Model): 
    transacoes = models.CharField(max_length = 10)
##Unidade de medida
class unit_measurement(models.Model):
    unidade_medida = models.CharField(max_length = 10)

##Tipos e subtipos
class Types(models.Model):
    tipo = models.CharField(max_length = 15)
class Subtype(models.Model):
    subtipo = models.CharField(max_length = 15)

class Manufacturer(models.Model):
    nome_fabricante = models.CharField(max_length = 15)

class MModel(models.Model):
    nome_modelo = models.CharField(max_length = 15)

class Brand(models.Model):
    nome_marca = models.CharField(max_length = 15)

class Product(models.Model):
    nome_produto = models.CharField(max_length = 15)
    marca_produto = models.CharField(max_length = 15)
    modelo_produto = models.CharField(max_length = 15)
    fabricante = models.CharField(max_length = 15)
    def __str__(self):
        return self.nome_produto
    
class Packaging_types(models.Model):
    nome_embalagem = models.CharField(max_length = 15)
    def __str__(self):
        return self.nome_embalagem

class Details_Product(models.Model):
    produto = models.ForeignKey(Product, related_name = 'details',on_delete = models.CASCADE)
    unidade_produto = models.IntegerField(default = 0)
    cor_produto = models.CharField(max_length = 10)
    sabor_produto = models.CharField(max_length = 15)
    quantidade_embalagem_produto = models.IntegerField
    tipo_embalagem_produto = models.ForeignKey(Packaging_types, related_name = 'packaging', on_delete = models.CASCADE)
    quantidade_produto = models.IntegerField(default = 0)
    preco_custo_produto = models.DecimalField(max_digits=6, decimal_places=2)
    preco_venda_produto = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return f"{self.produto.nome_produto}"
##Gerenciar Movimentacao
class movimentacao_produtos(models.Model): 
    data_hora_movimentacao = models.DateTimeField



