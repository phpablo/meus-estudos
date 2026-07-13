class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, equipe):
        super().__init__(nome, idade, salario)
        self.equipe = equipe

    def apresentar(self):
        super().apresentar()  # reaproveita comportamento da classe pai
        print(f"Sou gerente da equipe {self.equipe}.")

g1 = Gerente("Carlos", 45, 12000, "Desenvolvimento")
g1.apresentar()