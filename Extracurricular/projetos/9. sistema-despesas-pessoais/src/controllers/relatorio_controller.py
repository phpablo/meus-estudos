from datetime import date
from src.models.receita import Receita
from src.models.despesa import Despesa


class RelatorioController:
    def __init__(self, controller_lancamentos):
        # Ele precisa acessar os dados do outro controller para calcular
        self._controller_dados = controller_lancamentos

    def gerar_balanco_mensal(self, mes: int, ano: int):
        """
        Calcula o total de receitas, despesas e o saldo final de um mês específico.
        """
        total_receitas = 0.0
        total_despesas = 0.0

        lancamentos = self._controller_dados.listar_lancamentos()

        for l in lancamentos:
            # Filtra pelo mês e ano solicitados
            if l.data.month == mes and l.data.year == ano:
                if isinstance(l, Receita):
                    total_receitas += l.valor
                elif isinstance(l, Despesa):
                    total_despesas += l.valor

        saldo = total_receitas - total_despesas

        # Retorna um dicionário com o resumo (DTO)
        return {
            "mes": f"{mes}/{ano}",
            "total_receitas": total_receitas,
            "total_despesas": total_despesas,
            "saldo": saldo,
            "status": "DÉFICIT 🚨" if saldo < 0 else "SUPERÁVIT ✅"
        }

    def total_por_categoria(self, mes: int, ano: int):
        """
        Retorna quanto foi gasto em cada categoria naquele mês.
        """
        resumo = {}  # Ex: {'Lazer': 200.0, 'Mercado': 500.0}

        lancamentos = self._controller_dados.listar_lancamentos()

        for l in lancamentos:
            if isinstance(l, Despesa) and l.data.month == mes and l.data.year == ano:
                nome_cat = l.categoria.nome
                # Se já tem a categoria no resumo, soma. Se não, cria.
                resumo[nome_cat] = resumo.get(nome_cat, 0.0) + l.valor

        return resumo