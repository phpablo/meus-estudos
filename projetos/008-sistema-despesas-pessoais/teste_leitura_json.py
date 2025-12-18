from src.controllers.categoria_controller import CategoriaController
from src.controllers.lancamento_controller import LancamentoController
from src.controllers.relatorio_controller import RelatorioController

print("--- INICIANDO SISTEMA (Carregando do Disco...) ---")

# 1. Ao instanciar, eles vão ler os arquivos .json automaticamente
ctrl_cat = CategoriaController()
ctrl_lanc = LancamentoController()
ctrl_rel = RelatorioController(ctrl_lanc)

# 2. Testar se as Categorias voltaram
print("\n--- 📂 CATEGORIAS CARREGADAS ---")
categorias = ctrl_cat.listar_todas()
if not categorias:
    print("❌ Nenhuma categoria encontrada (O JSON está vazio ou não foi lido).")
else:
    for c in categorias:
        print(f"✅ {c.nome} ({c.tipo}) - Limite: {c.limite}")

# 3. Testar se os Lançamentos voltaram
print("\n--- 💸 LANÇAMENTOS CARREGADOS ---")
lancamentos = ctrl_lanc.listar_lancamentos()
if not lancamentos:
    print("❌ Nenhum lançamento encontrado.")
else:
    for l in lancamentos:
        print(f"✅ {l}")

# 4. Testar se o Relatório ainda funciona com os dados recuperados
print("\n--- 📊 RELATÓRIO DO MÊS 12/2025 ---")
# Nota: Só vai funcionar se você tiver salvo dados de dezembro no teste anterior
balanco = ctrl_rel.gerar_balanco_mensal(12, 2025)
print(f"Saldo Recuperado: R$ {balanco['saldo']:.2f}")