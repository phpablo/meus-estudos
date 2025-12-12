from abc import ABC, abstractmethod

# [ATIVIDADE] - 04 - Interfaces + injeção de dependência
class IGatewayPagamento(ABC):
    @abstractmethod
    def cobrar(self, valor):
        pass

class GatewayCartao(IGatewayPagamento):
    def cobrar(self,valor):
        return f"Cobrando R$ {valor:.2f} no cartão"

class GatewayPIX(IGatewayPagamento):
    def cobrar(self,valor):
        return f"Cobrando R$ {valor:.2f} no PIX"

class GatewayTeste(IGatewayPagamento):
    def __init__(self):
        self.ultimo_valor = None

    def cobrar(self,valor):
        self.ultimo_valor = valor
        return f"TESTE_OK:{self.ultimo_valor}"

class Pedido:
    def __init__(self,gateway = IGatewayPagamento):
        self.gateway = gateway

    def finalizar(self, valor):
        return self.gateway.cobrar(valor)

# ------------- TESTES MANUAIS -------------
if __name__ == "__main__":
    print("----- TESTE CARTÃO -----")
    pedido_cartao = Pedido(gateway=GatewayCartao())  # <- repare nos ()
    print(pedido_cartao.finalizar(100))

    print("\n----- TESTE PIX -----")
    pedido_pix = Pedido(gateway=GatewayPIX())
    print(pedido_pix.finalizar(75))

    print("\n----- TESTE AUTOMATIZADO -----")
    gt = GatewayTeste()
    pedido_teste = Pedido(gt)

    resultado = pedido_teste.finalizar(55)
    print("Retorno:", resultado)
    print("Último valor registrado:", gt.ultimo_valor)

    # asserts
    assert resultado == "TESTE_OK:55"
    assert gt.ultimo_valor == 55

    print("\nTODOS OS TESTES PASSARAM ✔️")