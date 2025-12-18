import json
import os
from datetime import date
from src.models.categoria import Categoria
from src.models.receita import Receita
from src.models.despesa import Despesa


class Persistencia:
    DIR_DADOS = "data"  # Pasta onde vamos salvar

    @staticmethod
    def _caminho_arquivo(nome_arquivo):
        # Garante que a pasta existe
        if not os.path.exists(Persistencia.DIR_DADOS):
            os.makedirs(Persistencia.DIR_DADOS)
        return os.path.join(Persistencia.DIR_DADOS, nome_arquivo)

    @staticmethod
    def salvar_categorias(lista_categorias):
        caminho = Persistencia._caminho_arquivo("categorias.json")
        lista_dicts = [c.to_dict() for c in lista_categorias]

        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(lista_dicts, f, indent=4, ensure_ascii=False)

    @staticmethod
    def carregar_categorias():
        caminho = Persistencia._caminho_arquivo("categorias.json")
        if not os.path.exists(caminho):
            return []

        with open(caminho, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            # Reconstrói os objetos Categoria
            return [Categoria.from_dict(d) for d in dados]

    @staticmethod
    def salvar_lancamentos(lista_lancamentos):
        caminho = Persistencia._caminho_arquivo("lancamentos.json")
        lista_dicts = [l.to_dict() for l in lista_lancamentos]

        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(lista_dicts, f, indent=4, ensure_ascii=False)

    @staticmethod
    def carregar_lancamentos():
        caminho = Persistencia._caminho_arquivo("lancamentos.json")
        if not os.path.exists(caminho):
            return []

        with open(caminho, 'r', encoding='utf-8') as f:
            dados_brutos = json.load(f)

        objetos = []
        for d in dados_brutos:
            # 1. Reconstrói a Categoria
            cat = Categoria.from_dict(d['categoria'])
            # 2. Converte a data de string para objeto date
            data_obj = date.fromisoformat(d['data'])

            # 3. Decide se cria Receita ou Despesa
            if d['classe'] == 'Receita':
                obj = Receita(d['valor'], cat, data_obj, d['descricao'], d['forma_pagamento'])
            elif d['classe'] == 'Despesa':
                obj = Despesa(d['valor'], cat, data_obj, d['descricao'], d['forma_pagamento'])

            objetos.append(obj)

        return objetos