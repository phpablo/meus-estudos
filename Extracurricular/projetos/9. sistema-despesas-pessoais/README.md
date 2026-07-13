# 💰 Sistema de Controle de Despesas Pessoais

> Projeto acadêmico da disciplina de Programação Orientada a Objetos (POO) - UFCA.

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![Status](https://img.shields.io/badge/status-em_desenvolvimento-orange)
![License](https://img.shields.io/badge/license-MIT-green)

## 📝 Visão Geral
Este é um sistema de linha de comando (CLI) projetado para auxiliar no gerenciamento de finanças pessoais. O sistema permite o controle de receitas, despesas e orçamentos, fornecendo relatórios automáticos e alertas inteligentes sobre a saúde financeira do usuário.

O projeto foi desenvolvido seguindo estritamente os pilares da **Orientação a Objetos** e o padrão de arquitetura **MVC (Model-View-Controller)**.

## 🎯 Funcionalidades Principais
Conforme especificação do projeto:

* **Gestão de Categorias:** Cadastro, edição e exclusão de categorias de receitas e despesas.
* **Lançamentos Financeiros:** Registro detalhado de ganhos e gastos (com validações de saldo e tipo).
* **Controle Orçamentário:** Definição de limites mensais e verificação de saldo disponível.
* **Alertas Automáticos:**
    * ⚠️ Despesas de alto valor (acima de R$ 500,00).
    * 🚫 Limite da categoria excedido.
    * 📉 Déficit orçamentário (saldo negativo).
* **Relatórios e Estatísticas:** Análise de gastos por categoria, forma de pagamento e comparativos mensais.
* **Persistência de Dados:** Armazenamento seguro das informações.

## 🛠️ Tecnologias e Conceitos Aplicados
* **Linguagem:** Python 3
* **Paradigma:** Programação Orientada a Objetos (POO)
    * *Herança e Polimorfismo*
    * *Encapsulamento (@property, @setter)*
    * *Abstração*
* **Arquitetura:** MVC (Model-View-Controller)
* **Testes:** Pytest

## 🚀 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone [https://github.com/phpablo/ufca_ads_2025_sistema_de_controle_de_despesas_pessoais.git](https://github.com/phpablo/ufca_ads_2025_sistema_de_controle_de_despesas_pessoais.git)