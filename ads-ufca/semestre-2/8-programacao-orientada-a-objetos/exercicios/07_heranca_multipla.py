class Diretor(Gerente):
    def __init__(self, nome, idade, salario, equipe, departamento):
        super().__init__(nome, idade, salario, equipe)
        self.departamento = departamento

    def apresentar(self):
        super().apresentar()
        print(f"Sou diretor do departamento de {self.departamento}.")

d1 = Diretor("Fernanda", 50, 20000, "Projetos", "TI")
d1.apresentar()