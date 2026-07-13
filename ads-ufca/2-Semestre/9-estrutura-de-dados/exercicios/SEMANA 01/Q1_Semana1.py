# 1. Crie uma classe chamada Ingresso, que possua o nome do evento e o valor do ingresso.
# Crie o método exibirValor(), que apenas retorne o valor do ingresso.
# Crie o método __str__ que retorne o nome do evento seguido do valor do ingresso.
# Crie um programa para testar sua classe.

class Ingresso:
    nome_evento = 'Baile de Inverno'
    valor_ingresso = 80

    def __str__(self):
        return f'Nome do evento: {self.nome_evento}\nValor do ingresso: {str(self.valor_ingresso)}'

    def exibir_valor(self):
        # return print(f' Valor do Ingresso é : R$ ' + str(self.valor_ingresso) + ' reais.')
        return print(f'O valor do ingresso é R$ {self.valor_ingresso} reais')



i1 = Ingresso()
i1.exibir_valor()

print(i1)


