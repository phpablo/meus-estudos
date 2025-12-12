
from __future__ import annotations
from dataclasses import dataclass
import json

class Produto:
    """Classe Produto com encapsulamento e formatação customizada.

    Atributos:
        id (int): identificador único (imutável após criação)
        nome (str): nome do produto
        preco (float): preço unitário >= 0
        moeda (str): código da moeda ("BRL" ou "USD")
        estoque (int): quantidade em estoque >= 0
    """
    __slots__ = ("_Produto__id", "_Produto__nome", "_Produto__preco", "_Produto__moeda", "_Produto__estoque")

    def __init__(self, id: int, nome: str, preco: float, moeda: str = "BRL", estoque: int = 0):
        # atributos "privados" (name-mangling)
        self.__id = None
        self.__nome = None
        self.__preco = None
        self.__moeda = None
        self.__estoque = None

        # setters centralizam validação
        self.__set_id_once(id)
        self.nome = nome
        self.preco = preco
        self.moeda = moeda
        self.estoque = estoque

    # ========= helpers internos =========
    def __set_id_once(self, valor: int):
        if self.__id is not None:
            raise AttributeError("id é imutável após criação")
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("id deve ser int >= 0")
        self.__id = valor

    @staticmethod
    def _fmt_brl(valor: float) -> str:
        # Formatação BRL: R$ 1.234,56 (sem depender de locale do SO)
        s = f"{valor:,.2f}"  # 1,234.56
        s = s.replace(",", "@").replace(".", ",").replace("@", ".")  # 1.234,56
        return f"R$ {s}"

    @staticmethod
    def _fmt_usd(valor: float) -> str:
        return f"$ {valor:,.2f}"

    def _fmt_currency(self, valor: float) -> str:
        if self.__moeda == "BRL":
            return self._fmt_brl(valor)
        elif self.__moeda == "USD":
            return self._fmt_usd(valor)
        # fallback genérico
        return f"{self.__moeda} {valor:,.2f}"

    # ========= properties (getters/setters) =========
    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("nome deve ser uma string não vazia")
        self.__nome = valor.strip()

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, valor: float) -> None:
        try:
            f = float(valor)
        except Exception:
            raise ValueError("preco deve ser numérico")
        if f < 0:
            raise ValueError("preco não pode ser negativo")
        self.__preco = f

    @property
    def moeda(self) -> str:
        return self.__moeda

    @moeda.setter
    def moeda(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor:
            raise ValueError("moeda deve ser string")
        valor = valor.upper()
        if valor not in {"BRL", "USD"}:
            raise ValueError("moeda inválida (use 'BRL' ou 'USD')")
        self.__moeda = valor

    @property
    def estoque(self) -> int:
        return self.__estoque

    @estoque.setter
    def estoque(self, valor: int) -> None:
        if isinstance(valor, bool):  # evita True/False como 1/0
            raise ValueError("estoque deve ser inteiro >= 0")
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("estoque deve ser inteiro >= 0")
        self.__estoque = valor

    @property
    def em_estoque(self) -> bool:
        return self.__estoque > 0

    # ========= métodos de domínio =========
    def aplicar_desconto(self, percentual: float) -> None:
        """Aplica desconto percentual (ex.: 10 -> 10%)."""
        try:
            p = float(percentual)
        except Exception:
            raise ValueError("percentual deve ser numérico")
        if not (0 <= p <= 100):
            raise ValueError("percentual deve estar entre 0 e 100")
        self.__preco = self.__preco * (1 - p/100.0)

    def aumentar_preco(self, valor: float) -> None:
        v = float(valor)
        if v < 0:
            raise ValueError("valor deve ser >= 0")
        self.__preco += v

    def diminuir_preco(self, valor: float) -> None:
        v = float(valor)
        if v < 0:
            raise ValueError("valor deve ser >= 0")
        novo = self.__preco - v
        if novo < 0:
            raise ValueError("preço não pode ficar negativo")
        self.__preco = novo

    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "nome": self.__nome,
            "preco": round(self.__preco, 2),
            "moeda": self.__moeda,
            "estoque": self.__estoque,
            "em_estoque": self.em_estoque,
        }

    # ========= representações =========
    def __repr__(self) -> str:
        return (f"Produto(id={self.__id}, nome={self.__nome!r}, preco={self.__preco:.2f}, "
                f"moeda={self.__moeda}, estoque={self.__estoque})")

    def __str__(self) -> str:
        return f"{self.__nome} ({self._fmt_currency(self.__preco)})"

    def __format__(self, spec: str) -> str:
        """Formatação customizada.

        Exemplos:
            f"{p}"              -> padrão (nome + preço)
            f"{p:full}"         -> detalhado
            f"{p:p}"            -> só preço formatado
            f"{p:nome}"         -> só nome
            f"{p:json}"         -> JSON
        """
        spec = (spec or "").strip().lower()
        if spec in ("", "s", None):
            return str(self)
        if spec == "full":
            return (f"Produto[id={self.__id}, nome='{self.__nome}', "
                    f"preco={self._fmt_currency(self.__preco)}, estoque={self.__estoque}, moeda={self.__moeda}]")
        if spec == "p" or spec == "preco" or spec == "price":
            return self._fmt_currency(self.__preco)
        if spec == "nome" or spec == "name":
            return self.__nome
        if spec == "json":
            return json.dumps(self.to_dict(), ensure_ascii=False)
        # fallback: retorna __str__ se o spec não for reconhecido
        return str(self)


p = Produto(id=1, nome="Câmera 4K", preco=1999.90, moeda="BRL", estoque=5)
print("__repr__ ->", repr(p))
print("__str__  ->", str(p))
print("format :p ->", f"{p:p}")         # preço
print("format :full ->", f"{p:full}")   # detalhado
print("format :json ->", f"{p:json}")   # json

# getters/setters
p.nome = "Câmera 4K Pro"
p.aplicar_desconto(10)   # 10% off
p.aumentar_preco(50)     # +50
print("Após ajustes:", f"{p:full}")



# def tenta(msg, fn):
#     try:
#         fn()
#     except Exception as e:
#         print(f"{msg}:", type(e).__name__, '-', e)
#
# tenta("nome vazio", lambda: Produto(2, " ", 10.0))
# tenta("preço negativo", lambda: Produto(3, "Item", -5.0))
# tenta("moeda inválida", lambda: Produto(4, "Item", 10.0, moeda="EUR"))
# tenta("estoque negativo", lambda: Produto(5, "Item", 10.0, estoque=-1))
#
# p2 = Produto(6, "Mouse", 100.0)
# tenta("id imutável", lambda: setattr(p2, "id", 123))  # não há setter público
