class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # chama o construtor da classe pai
        self.curso = curso # pertence à classe Estudante
    def estudar(self):
        print(f"{self.nome} está estudando {self.curso}.")

# Demonstração
p1 = Pessoa("Maria", 30)
e1 = Estudante("João", 20, "Engenharia")

p1.apresentar()
e1.apresentar()  # herdado da classe Pessoa
e1.estudar()