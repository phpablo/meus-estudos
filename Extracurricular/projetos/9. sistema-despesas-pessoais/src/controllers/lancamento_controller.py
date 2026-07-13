from datetime import date
from src.models.receita import Receita
from src.models.despesa import Despesa
from src.models.alerta import Alerta
from src.models.categoria import Categoria
from src.utils.persistencia import Persistencia  # <--- IMPORTANTE: Importar a persistência


class LancamentoController:
    def __init__(self):
        # Tenta carregar dados antigos ao iniciar
        self._lancamentos = Persistencia.carregar_lancamentos()
        self._alertas = []

    def adicionar_lancamento(self, valor: float, categoria: Categoria, data_lancamento: date, descricao: str,
                             forma_pagamento: str):

        novo_lancamento = None

        if categoria.tipo == "RECEITA":
            novo_lancamento = Receita(valor, categoria, data_lancamento, descricao, forma_pagamento)

        elif categoria.tipo == "DESPESA":
            novo_lancamento = Despesa(valor, categoria, data_lancamento, descricao, forma_pagamento)
            self._verificar_alertas_despesa(novo_lancamento)

        else:
            raise ValueError("Tipo de categoria desconhecido.")

        # Adiciona na lista da memória
        self._lancamentos.append(novo_lancamento)

        # --- AQUI ESTAVA O ERRO ---
        # Salva imediatamente no arquivo JSON
        Persistencia.salvar_lancamentos(self._lancamentos)

        return novo_lancamento

    def _verificar_alertas_despesa(self, despesa: Despesa):
        # (Código igual ao anterior, mantendo a lógica de alertas...)
        if despesa.valor > 500:
            msg = f"Despesa de alto valor detectada: R$ {despesa.valor:.2f} em {despesa.categoria.nome}"
            self._registrar_alerta(msg, despesa.categoria.nome)

        if despesa.categoria.limite > 0:
            total_gasto = self._calcular_total_gasto_categoria(despesa.categoria)
            total_previsto = total_gasto + despesa.valor

            if total_previsto > despesa.categoria.limite:
                excesso = total_previsto - despesa.categoria.limite
                msg = f"Limite da categoria '{despesa.categoria.nome}' excedido em R$ {excesso:.2f}!"
                self._registrar_alerta(msg, despesa.categoria.nome)

    def _calcular_total_gasto_categoria(self, categoria: Categoria) -> float:
        total = 0.0
        for l in self._lancamentos:
            if isinstance(l, Despesa) and l.categoria.nome == categoria.nome:
                total += l.valor
        return total

    def _registrar_alerta(self, mensagem, categoria_nome):
        alerta = Alerta(mensagem, categoria_nome)
        self._alertas.append(alerta)
        print(f"🔔 {alerta}")

    def listar_lancamentos(self):
        return self._lancamentos

    def listar_alertas(self):
        return self._alertas