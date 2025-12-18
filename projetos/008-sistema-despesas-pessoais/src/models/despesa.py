from .lancamento import Lancamento

class Despesa(Lancamento):
    def __init__(self, valor, categoria, data_lancamento, descricao, forma_pagamento):
        super().__init__(valor, categoria, data_lancamento, descricao, forma_pagamento)
        # Validação extra: Categoria deve ser do tipo DESPESA
        if categoria.tipo != "DESPESA":
            raise ValueError("Uma Despesa deve ter uma categoria do tipo 'DESPESA'.")