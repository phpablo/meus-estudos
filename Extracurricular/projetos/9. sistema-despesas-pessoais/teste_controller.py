from src.controllers.categoria_controller import CategoriaController

# 1. Instanciamos o Gerente
controller = CategoriaController()

print("--- Teste 1: Criando Categorias Normais ---")
try:
    cat1 = controller.criar_categoria("Alimentação", "DESPESA", limite=600.0)
    print(f"✅ Criado: {cat1}")

    cat2 = controller.criar_categoria("Salário", "RECEITA")
    print(f"✅ Criado: {cat2}")
except Exception as e:
    print(f"❌ Erro inesperado: {e}")

print("\n--- Teste 2: Tentando Duplicar (Deve falhar) ---")
try:
    # Tenta criar "Alimentação" de novo (mesmo com letra minúscula/maiúscula misturada)
    controller.criar_categoria("alimentação", "DESPESA", limite=1000.0)
    print("❌ FALHA: O sistema permitiu duplicar!")
except ValueError as e:
    print(f"✅ SUCESSO! O sistema barrou: {e}")

print("\n--- Teste 3: Listando Tudo ---")
for c in controller.listar_todas():
    print(f"- {c}")