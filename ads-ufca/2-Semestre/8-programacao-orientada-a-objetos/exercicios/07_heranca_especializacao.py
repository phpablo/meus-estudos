class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):  # sobrescrita de método
        print(f"Sou {self.nome}, tenho {self.idade} anos e ganho R$ {self.salario:.2f}.")

f1 = Funcionario("Ana", 40, 8500)
f1.apresentar()