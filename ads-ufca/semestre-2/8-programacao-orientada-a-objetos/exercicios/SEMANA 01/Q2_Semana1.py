# 2. Crie uma classe chamada Retangulo, a qual possua os atributos largura(b) e altura(h), e os métodos calcularPerimetro()
# e calcularArea().
# No código de teste, crie um objeto e calcule, respectivamente, o perímetro e a área desse retângulo.
class Retangulo:
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * self.largura + self.altura

retangulo_1 = Retangulo(4,10)
print(f' Área do retangulo é {retangulo_1.calcular_area()}')
print(f' O perimetro do retangulo é {retangulo_1.calcular_perimetro()}')
