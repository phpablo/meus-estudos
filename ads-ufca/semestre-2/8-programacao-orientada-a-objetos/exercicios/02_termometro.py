class Termometro:

    def __init__(self,valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self,valor):
        self.__valor = valor

    def aumentar(self,valor):
        self.__valor += valor

    def diminuir(self,valor):
        if self.valor == -273.15:
            print(f'Não é permitido temperatura abaixo do zero absoluto')
        else:
            self.__valor -= valor

    def mostrar(self):
        print(f'Temperatura: {self.valor} ºC')

    def em_fahrenheit(self):
        fahrenheit = self.__valor * 1.8 + 32
        print(f'{fahrenheit}')

t = Termometro(25)
t.mostrar()
t.aumentar(10)
t.mostrar()
t.valor = -300