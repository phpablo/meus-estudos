class Animal:
    def emitir_som(self):
        raise NotImplementedError("Método não implementa o emitir_som")

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"

c = Cachorro()
print(f"{c.__class__.__name__} diz: {c.emitir_som()}")