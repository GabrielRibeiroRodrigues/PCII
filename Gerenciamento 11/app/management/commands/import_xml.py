import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from app.models import *

class Command(BaseCommand):
    help = 'Importa dados de um arquivo XML para o banco de dados'

    def add_arguments(self, parser):
        parser.add_argument('xml_file', type=str)

    def handle(self, *args, **kwargs):
        xml_file = kwargs['xml_file']
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Importar marcas
        for marca_element in root.findall('Marca'):
            nome_marca = marca_element.find('nome_marca')
            if nome_marca is not None:
                nome_marca = nome_marca.text
                Marca.objects.get_or_create(nome_marca=nome_marca)

        # Importar produtos
        for produto_element in root.findall('Produto'):
            nome_produto = produto_element.find('nome_produto')
            marca_nome = produto_element.find('marca')
            modelo_nome = produto_element.find('modelo')
            fabricante_nome = produto_element.find('fabricante')

            if nome_produto is not None:
                nome_produto = nome_produto.text
            if marca_nome is not None:
                marca_nome = marca_nome.text
                marca, _ = Marca.objects.get_or_create(nome_marca=marca_nome)
            else:
                marca = None

            if modelo_nome is not None:
                modelo_nome = modelo_nome.text
                modelo, _ = Modelo.objects.get_or_create(nome_modelo=modelo_nome)
            else:
                modelo = None

            if fabricante_nome is not None:
                fabricante_nome = fabricante_nome.text
                fabricante, _ = Fabricante.objects.get_or_create(nome_fabricante=fabricante_nome)
            else:
                fabricante = None

            produto, _ = Produto.objects.get_or_create(
                nome_produto=nome_produto,
                marca=marca,
                modelo=modelo,
                fabricante=fabricante
            )

            # Importar detalhes do produto
            for detalhe_element in produto_element.findall('DetalheProduto'):
                cor_produto = detalhe_element.find('cor_produto')
                sabor_produto = detalhe_element.find('sabor_produto')
                quantidade_embalagem_produto = detalhe_element.find('quantidade_embalagem_produto')
                tipo_embalagem_nome = detalhe_element.find('tipo_embalagem_produto')
                quantidade_produto = detalhe_element.find('quantidade_produto')
                preco_custo_produto = detalhe_element.find('preco_custo_produto')
                preco_venda_produto = detalhe_element.find('preco_venda_produto')
                subsetor_nome = detalhe_element.find('subsetor')
                setor_nome = detalhe_element.find('setor')

                if cor_produto is not None:
                    cor_produto = cor_produto.text
                if sabor_produto is not None:
                    sabor_produto = sabor_produto.text
                if quantidade_embalagem_produto is not None:
                    quantidade_embalagem_produto = int(quantidade_embalagem_produto.text or 0)
                if tipo_embalagem_nome is not None:
                    tipo_embalagem_nome = tipo_embalagem_nome.text
                    tipo_embalagem, _ = TipoEmbalagem.objects.get_or_create(nome_embalagem=tipo_embalagem_nome)
                else:
                    tipo_embalagem = None
                if quantidade_produto is not None:
                    quantidade_produto = int(quantidade_produto.text or 0)
                if preco_custo_produto is not None:
                    preco_custo_produto = float(preco_custo_produto.text or 0.0)
                if preco_venda_produto is not None:
                    preco_venda_produto = float(preco_venda_produto.text or 0.0)
                if subsetor_nome is not None:
                    subsetor_nome = subsetor_nome.text
                if setor_nome is not None:
                    setor_nome = setor_nome.text
                    setor, _ = Sector.objects.get_or_create(nome_setor=setor_nome)
                else:
                    setor = None

                if subsetor_nome and setor:
                    subsetor, _ = Subsector.objects.get_or_create(nome_sub_setor=subsetor_nome, setor=setor)

                    DetalheProduto.objects.get_or_create(
                        produto=produto,
                        cor_produto=cor_produto,
                        sabor_produto=sabor_produto,
                        quantidade_embalagem_produto=quantidade_embalagem_produto,
                        tipo_embalagem_produto=tipo_embalagem,
                        quantidade_produto=quantidade_produto,
                        preco_custo_produto=preco_custo_produto,
                        preco_venda_produto=preco_venda_produto,
                        subsetor=subsetor
                    )

        self.stdout.write(self.style.SUCCESS('Dados importados com sucesso'))
