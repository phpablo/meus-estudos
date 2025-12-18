import os
from datetime import date, datetime
from src.controllers.categoria_controller import CategoriaController
from src.controllers.lancamento_controller import LancamentoController
from src.controllers.relatorio_controller import RelatorioController


class MenuPrincipal:
    def __init__(self):
        # Instancia os controllers
        self.ctrl_cat = CategoriaController()
        self.ctrl_lanc = LancamentoController()
        self.ctrl_rel = RelatorioController(self.ctrl_lanc)

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def exibir_titulo(self):
        print("=" * 40)
        print("💰 SISTEMA DE CONTROLE FINANCEIRO")
        print("=" * 40)

    def iniciar(self):
        while True:
            self.limpar_tela()  # <--- ADICIONE ESTA LINHA AQUI
            self.exibir_titulo()
            print("1. Cadastrar Categoria")
            print("2. Novo Lançamento (Receita/Despesa)")
            print("3. Ver Relatório Mensal")
            print("4. Listar Tudo (Categorias/Lançamentos)")
            print("0. Sair")
            print("-" * 40)

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self._menu_criar_categoria()
            elif opcao == '2':
                self._menu_novo_lancamento()
            elif opcao == '3':
                self._menu_relatorio()
            elif opcao == '4':
                self._menu_listar_tudo()
            elif opcao == '0':
                print("Saindo... Até logo! 👋")
                break
            else:
                print("Opção inválida!")
                input("Pressione Enter para continuar...")
                # Não precisa chamar limpar_tela aqui embaixo mais,
                # pois o loop vai voltar pro começo e limpar.

    # --- SUB-MENUS ---

    def _menu_criar_categoria(self):
        self.limpar_tela()
        print("--- 📂 NOVA CATEGORIA ---")
        nome = input("Nome da Categoria: ")
        tipo = input("Tipo (RECEITA ou DESPESA): ").upper()

        limite = 0.0
        if tipo == 'DESPESA':
            try:
                limite = float(input("Limite Mensal (R$): "))
            except ValueError:
                limite = 0.0

        try:
            self.ctrl_cat.criar_categoria(nome, tipo, limite)
            print("✅ Categoria criada com sucesso!")
        except Exception as e:
            print(f"❌ Erro: {e}")

        input("\nPressione Enter para voltar...")
        self.limpar_tela()

    def _menu_novo_lancamento(self):
        self.limpar_tela()
        print("--- 💸 NOVO LANÇAMENTO ---")

        # 1. Selecionar Categoria
        categorias = self.ctrl_cat.listar_todas()
        if not categorias:
            print("❌ Nenhuma categoria cadastrada. Crie uma antes.")
            input("Enter para voltar...")
            return

        print("Selecione a Categoria:")
        for i, cat in enumerate(categorias):
            tipo_icon = "+" if cat.tipo == "RECEITA" else "-"
            print(f"[{i}] {cat.nome} ({tipo_icon})")

        try:
            idx = int(input("Número da Categoria: "))
            categoria_escolhida = categorias[idx]
        except:
            print("❌ Seleção inválida.")
            return

        # 2. Dados do Lançamento
        try:
            valor = float(input("Valor (R$): "))
            descricao = input("Descrição: ")
            pagamento = input("Forma de Pagamento (Pix, Dinheiro...): ")

            # Data (Assume hoje para facilitar, mas poderia pedir)
            data_hoje = date.today()

            self.ctrl_lanc.adicionar_lancamento(
                valor, categoria_escolhida, data_hoje, descricao, pagamento
            )
            print("✅ Lançamento registrado!")

            # Verifica se gerou alertas
            alertas = self.ctrl_lanc.listar_alertas()
            if alertas and not alertas[-1].visto:  # Mostra só o último se for novo
                print(f"\n⚠️  ALERTA DO SISTEMA: {alertas[-1].mensagem}")
                alertas[-1].visto = True

        except ValueError as e:
            print(f"❌ Erro de valor: {e}")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

        input("\nEnter para voltar...")
        self.limpar_tela()

    def _menu_relatorio(self):
        self.limpar_tela()
        print("--- 📊 RELATÓRIO MENSAL ---")
        try:
            mes = int(input("Mês (1-12): "))
            ano = int(input("Ano (ex: 2025): "))

            dados = self.ctrl_rel.gerar_balanco_mensal(mes, ano)

            print("\n" + "-" * 30)
            print(f"RESUMO DE {mes}/{ano}")
            print(f"Receitas: R$ {dados['total_receitas']:.2f}")
            print(f"Despesas: R$ {dados['total_despesas']:.2f}")
            print(f"SALDO:    R$ {dados['saldo']:.2f}")
            print(f"Status:   {dados['status']}")
            print("-" * 30)

        except ValueError:
            print("Data inválida.")

        input("\nEnter para voltar...")
        self.limpar_tela()

    def _menu_listar_tudo(self):
        self.limpar_tela()
        print("--- 📂 TODAS AS CATEGORIAS ---")
        for c in self.ctrl_cat.listar_todas():
            print(f"- {c.nome} ({c.tipo}) Limite: R$ {c.limite}")

        print("\n--- 💸 ÚLTIMOS LANÇAMENTOS ---")
        for l in self.ctrl_lanc.listar_lancamentos():
            print(l)

        input("\nEnter para voltar...")
        self.limpar_tela()