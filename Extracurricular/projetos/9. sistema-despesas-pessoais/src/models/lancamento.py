from datetime import date
from .categoria import Categoria

class Lancamento:
    def __init__(self, valor: float, categoria: Categoria, data_lancamento: date, descricao: str, forma_pagamento: str):
        self._valor = 0.0  # Inicializa seguro
        self.valor = valor  # Usa o setter para validar imediatamente

        self._categoria = categoria
        self._data = data_lancamento
        self._descricao = descricao
        self._forma_pagamento = forma_pagamento

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        # Regra: Não é permitido cadastrar despesas/receitas com valor <= 0 [cite: 23, 78]
        if novo_valor <= 0:
            raise ValueError("O valor do lançamento deve ser maior que zero.")
        self._valor = novo_valor

    @property
    def categoria(self):
        return self._categoria

    @property
    def data(self):
        return self._data

    # Métodos Mágicos exigidos no PDF [cite: 50]
    def __str__(self):
        return f"{self.data} | {self._descricao}: R$ {self.valor:.2f} [{self.categoria.nome}]"

    def __repr__(self):
        return f"Lancamento(valor={self.valor}, categoria='{self.categoria.nome}', data='{self.data}')"

    # Ordenação por data (para relatórios) [cite: 56]
    def __lt__(self, other):
        return self.data < other.data

    def to_dict(self):
        return {
            "classe": self.__class__.__name__,  # Guarda se é 'Receita' ou 'Despesa'
            "valor": self.valor,
            "categoria": self.categoria.to_dict(),  # Salva a categoria aninhada
            "data": self.data.isoformat(),  # Converte data para string "YYYY-MM-DD"
            "descricao": self._descricao,
            "forma_pagamento": self._forma_pagamento
        }