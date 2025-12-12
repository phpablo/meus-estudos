class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        return f"Olá, eu sou {self.nome}"

class Funcionario(Pessoa):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario

    def calcular_salario(self):
        return self.salario

    def apresentar(self):
        return super().apresentar() + f". Sou funcionário e ganho R${self.salario}"

class Estudante(Pessoa):
    def __init__(self, nome, curso, bolsa=0.0, *args, **kwargs):
        super().__init__(nome, *args, **kwargs)
        self.curso = curso
        self.bolsa = bolsa

    def calcular_bolsa(self):
        return self.bolsa

    def apresentar(self):
        return super().apresentar() + f". Sou estudante do curso de {self.curso}"


class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe, *args, **kwargs):
        super().__init__(nome, salario, *args, **kwargs)
        self.equipe = equipe

    def apresentar(self):
        return super().apresentar() + f". Gerencio uma equipe de {len(self.equipe)} pessoas"


class AssistentePesquisa(Estudante, Funcionario):
    def __init__(self, nome, curso, salario, bolsa=0.0, *args, **kwargs):
        super().__init__(nome, curso, bolsa, salario, *args, **kwargs)

    def apresentar(self):
        return super().apresentar() + ". Sou assistente de pesquisa"