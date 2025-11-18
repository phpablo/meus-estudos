class Pessoa:
    def salvar_dados (self,nome,idade,altura,peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def apresentar(self):
        print(f'Olá meu nome é {self.nome}')

p1 = Pessoa()
p1.salvar_dados('Gohan', 12, 1.60, 60)
p1.apresentar()


