from .lancamento import Lancamento

class Receita(Lancamento):
    def __init__(self, valor, categoria, data_lancamento, descricao, forma_pagamento):
        super().__init__(valor, categoria, data_lancamento, descricao, forma_pagamento)
        # Validação extra: Categoria deve ser do tipo RECEITA
        if categoria.tipo != "RECEITA":
            raise ValueError("Uma Receita deve ter uma categoria do tipo 'RECEITA'.")