from datetime import date
from src.controllers.categoria_controller import CategoriaController
from src.controllers.lancamento_controller import LancamentoController

# Instancia os controllers
ctrl_cat = CategoriaController()
ctrl_lanc = LancamentoController()

print("--- 1. Limpando dados antigos (se houver) ---")
# Hackzinho: Acessando a lista interna protegida só para limpar
ctrl_cat._categorias = []
ctrl_lanc._lancamentos = []

print("--- 2. Recriando Categorias ---")
# Ao criar, ele já vai salvar automaticamente no JSON
cat_salario = ctrl_cat.criar_categoria("Salário", "RECEITA")
cat_moradia = ctrl_cat.criar_categoria("Moradia", "DESPESA", limite=1200.0)
cat_lazer = ctrl_cat.criar_categoria("Lazer", "DESPESA", limite=200.0)

print("--- 3. Recriando Lançamentos ---")
hoje = date.today()

# Salário
ctrl_lanc.adicionar_lancamento(4000.0, cat_salario, hoje, "Salário Mensal", "Pix")
print("✅ Salário salvo.")

# Aluguel
ctrl_lanc.adicionar_lancamento(1200.0, cat_moradia, hoje, "Aluguel", "Pix")
print("✅ Aluguel salvo.")

# Lazer (Estourando limite de propósito para testar)
ctrl_lanc.adicionar_lancamento(300.0, cat_lazer, hoje, "Churrasco", "Crédito")
print("✅ Churrasco salvo.")

print("\n🎉 BANCO DE DADOS POPULADO COM SUCESSO!")
print("Agora rode o arquivo 'teste_leitura_json.py' novamente.")