

class Pessoa:
    def __init__(self,nome, **kwargs):
        self.nome = nome

    def apresentar(self):
        return f"Olá,eu sou {self.nome}"

class Funcionario(Pessoa):
    def __init__(self,nome:str, salario : float, **kwargs):
        super().__init__(nome=nome,**kwargs)
        self.salario = salario

    def calcular_salario(self):
        return self.salario

    def apresentar(self):
        return f"Olá, eu sou {self.nome} e sou funcionário. Meu salário é {self.salario}"

class Estudante(Pessoa):
    def __init__(self,nome:str,curso:str,bolsa:float = 0.0, **kwargs):
        super().__init__(nome=nome,**kwargs)
        self.curso = curso
        self.bolsa = bolsa

    def calcular_bolsa(self):
        return self.bolsa

    def apresentar(self):
        return f"Olá, eu sou {self.nome}, sou estudante do curso de {self.curso} e minha bolsa é {self.bolsa}"

class Gerente(Funcionario):
    def __init__(self,nome:str,salario:float,equipe:list, **kwargs):
        super().__init__(nome=nome,salario=salario,**kwargs)
        self.equipe = equipe

    def apresentar(self):
        # return (f"Olá, eu sou {self.nome}, sou gerente, meu salário é {self.salario}, "
        #         f"e gerencio uma equipe de {len(self.equipe)} pessoas.")
        return (f"Olá, eu sou {self.nome}, sou gerente, meu salário é {self.salario}"
                f"e gerencio uma equipe de {len(self.equipe)} pessoas.")

class AssistentePesquisa(Estudante, Funcionario):
    def __init__(self, nome, curso, salario, bolsa=0.0,**kwargs):
        super().__init__(nome=nome, curso=curso, bolsa=bolsa, salario=salario, **kwargs)

    def apresentar(self):
        return (f"Olá, eu sou {self.nome}, assistente de pesquisa, "
                f"estudante de {self.curso}, recebo bolsa de {self.bolsa} "
                f"e também tenho salário de {self.salario}.")

# --- testes rápidos ---
if __name__ == "__main__":
    p = Pessoa("Ana")
    f = Funcionario("João", 5000)
    e = Estudante("Maria", "Computação", bolsa=300)
    g = Gerente("Carlos", 8000, ["Ana", "João"])
    a = AssistentePesquisa("Bulma", "Engenharia", salario=7000, bolsa=1200)

    print(p.apresentar())
    print(f.apresentar(), f.calcular_salario())
    print(e.apresentar(), e.calcular_bolsa())
    print(g.apresentar())
    print(a.apresentar())

    # cheque de tipo / atributos
    assert isinstance(a, Estudante)
    assert isinstance(a, Funcionario)
    assert a.salario == 7000.0
    assert a.bolsa == 1200.0

    # ver MRO para confirmação
    print("MRO:", AssistentePesquisa.__mro__)
