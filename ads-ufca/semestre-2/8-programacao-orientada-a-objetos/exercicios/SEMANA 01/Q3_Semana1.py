# 3. Crie uma classe Ponto, conforme a figura a seguir.
# O método __str__ deve retornar os atributos do objeto no formato “nome: (x, y)”.
#  Crie em outro arquivo os testes para a classe Ponto,
#  lendo diversos pontos e criando um objeto ponto para cada entrada lida.
#  Coloque cada objeto da classe Ponto em uma lista e, ao final, imprima cada elemento dessa lista.

class Ponto:
    def __init__(self,nome,x,y):
        self.nome = nome
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.nome}: ({self.x}, {self.y})'