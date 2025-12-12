# [ATIVIDADE] - 04 - Interfaces + injeção de dependência
from abc import ABC, abstractmethod

# ------------------------------
#      ÁREA DO ALUNO
# ------------------------------

class IGatewayPagamento(ABC):
    @abstractmethod
    def cobrar(self, valor):
        pass


class GatewayCartao(IGatewayPagamento):
    def cobrar(self, valor):
        return f"Cobrando R$ {valor:.2f} no cartão"


class GatewayPIX(IGatewayPagamento):
    def cobrar(self, valor):
        return f"Enviando cobrança PIX de R$ {valor:.2f}"


class GatewayTeste(IGatewayPagamento):
    def __init__(self):
        self.ultimo_valor = None

    def cobrar(self, valor):
        self.ultimo_valor = valor
        return f"TESTE_OK:{valor}"


class Pedido:
    def __init__(self, gateway: IGatewayPagamento):
        self.gateway = gateway

    def finalizar(self, valor):
        return self.gateway.cobrar(valor)


# ------------------------------
#      ÁREA DO PROFESSOR
#     (NÃO ALTERAR)
# ------------------------------
if __name__ == "__main__":
    print("### Teste Manual ###")

    pedido_cartao = Pedido(GatewayCartao())
    print(pedido_cartao.finalizar(50))

    pedido_pix = Pedido(GatewayPIX())
    print(pedido_pix.finalizar(87.90))

    # Teste com gateway de teste
    gtest = GatewayTeste()
    pedido_teste = Pedido(gtest)
    r = pedido_teste.finalizar(123)

    print("Retorno:", r)
    print("Último valor registrado:", gtest.ultimo_valor)

    assert r == "TESTE_OK:123"
    assert gtest.ultimo_valor == 123

    print("PASSOU EM TODOS OS TESTES!")
