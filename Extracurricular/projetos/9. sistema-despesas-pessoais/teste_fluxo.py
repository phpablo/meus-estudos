from datetime import date
from src.controllers.categoria_controller import CategoriaController
from src.controllers.lancamento_controller import LancamentoController
from src.controllers.relatorio_controller import RelatorioController # <--- Nova Importação

# 1. Inicializa os Controllers
ctrl_cat = CategoriaController()
ctrl_lanc = LancamentoController()
ctrl_relatorio = RelatorioController(ctrl_lanc) # <--- Conectamos o Relatório aos Lançamentos

print("--- CADASTRO DE DADOS ---")
# Criando Categorias
cat_salario = ctrl_cat.criar_categoria("Salário", "RECEITA")
cat_aluguel = ctrl_cat.criar_categoria("Moradia", "DESPESA", limite=1200.0)
cat_lazer = ctrl_cat.criar_categoria("Lazer", "DESPESA", limite=200.0)

# Criando Lançamentos (Mês 12/2025)
hoje = date(2025, 12, 15)

# Ganha 3000
ctrl_lanc.adicionar_lancamento(3000.0, cat_salario, hoje, "Salário", "Pix")

# Gasta 1200 (Aluguel)
ctrl_lanc.adicionar_lancamento(1200.0, cat_aluguel, hoje, "Aluguel Apto", "Pix")

# Gasta 2000 (Lazer - Ops! Gastou mais do que podia e mais do que tinha)
# Isso deve gerar Alerta de Limite E Alerta de Déficit no final
ctrl_lanc.adicionar_lancamento(2000.0, cat_lazer, hoje, "Viagem Impulsiva", "Crédito")

print("\n--- 📊 RELATÓRIO MENSAL (DEZEMBRO/2025) ---")
balanco = ctrl_relatorio.gerar_balanco_mensal(12, 2025)

print(f"Receitas: R$ {balanco['total_receitas']:.2f}")
print(f"Despesas: R$ {balanco['total_despesas']:.2f}")
print(f"Saldo:    R$ {balanco['saldo']:.2f}")
print(f"Status:   {balanco['status']}")

# Verificação Extra: Alerta de Déficit
if balanco['saldo'] < 0:
    print("\n🚨 ALERTA CRÍTICO: Você gastou mais do que ganhou!")

print("\n--- 🍰 GASTOS POR CATEGORIA ---")
por_cat = ctrl_relatorio.total_por_categoria(12, 2025)
for categoria, valor in por_cat.items():
    print(f"{categoria}: R$ {valor:.2f}")