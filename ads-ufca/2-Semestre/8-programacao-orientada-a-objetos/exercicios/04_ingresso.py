class Ingresso:
    def __init__(self,nome_evento,valor_ingresso):
        self.nome_evento = nome_evento
        self.valor_ingresso = valor_ingresso

    def exibir_valor(self):
        return self.valor_ingresso

    def __str__(self):
        valor = self.exibir_valor()
        return f'Evento: {self.nome_evento} - Valor ingresso: {valor}'

evento1 = Ingresso('ExpoBrás', 99)
print(evento1)