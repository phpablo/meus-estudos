# ======== ÁREA DO ALUNO ========

class Produto:
    # implemente aqui a classe Produto
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome deve ser uma string não vazia.")
        self.__nome = valor.strip()

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("O preço deve ser um número maior ou igual a zero.")
        self.__preco = float(valor)

    def __str__(self):
        return f"{self.nome} - {self.preco:.2f}"


class Cliente:
    # implemente aqui a classe Cliente
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome deve ser uma string não vazia.")
        self.__nome = valor.strip()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if not isinstance(valor, str) or '@' not in valor or '.' not in valor:
            raise ValueError("O email deve conter o caractere '@' e pelo menos um '.'.")
        self.__email = valor

    def __str__(self):
        return f"{self.nome} <{self.email}>"

# ======== ÁREA DO PROFESSOR / TESTES ========
# !!!!!! NÃO MEXA AQUI !!!! PODE AFETAR SUA NOTA

def cmd_ok():
    try:
        p = Produto("Câmera", 1999.90)
        c = Cliente("Ana", "ana@ex.com")
        return f"{p}\n{c}"
    except Exception as e:
        return f"ERRO: {e}"

def cmd_set_ok():
    try:
        p = Produto("X", 10)
        p.nome = "Cam Pro"
        p.preco = 1499.9
        return f"{p.nome}:{p.preco}"
    except Exception as e:
        return f"ERRO: {e}"

def cmd_set_bad_nome():
    try:
        p = Produto("X", 10)
        p.nome = " "
        return "ERRO_NAO_LANCADO"
    except Exception:
        return "ERRO_ESPERADO"

def cmd_set_bad_preco():
    try:
        p = Produto("X", 10)
        p.preco = -1
        return "ERRO_NAO_LANCADO"
    except Exception:
        return "ERRO_ESPERADO"

def cmd_email_bad():
    try:
        _ = Cliente("Ana", "inválido")
        return "ERRO_NAO_LANCADO"
    except Exception:
        return "ERRO_ESPERADO"

def cmd_ctor_bad_nome():
    try:
        _ = Produto("", 10)
        return "ERRO_NAO_LANCADO"
    except Exception:
        return "ERRO_ESPERADO"

def cmd_ctor_bad_preco():
    try:
        _ = Produto("X", -5)
        return "ERRO_NAO_LANCADO"
    except Exception:
        return "ERRO_ESPERADO"

def cmd_mangled():
    try:
        p = Produto("Y", 1)
        has_direct = hasattr(p, "__nome")
        has_mangled = hasattr(p, "_Produto__nome") and hasattr(p, "_Produto__preco")
        if not has_direct and has_mangled:
            return "NO_DIRECT\nMANGLED_OK"
        else:
            return "MANGLED_FAIL"
    except Exception as e:
        return f"ERRO: {e}"

def cmd_direct():
    try:
        p = Produto("Z", 5)
        _ = p.__nome  # deve falhar
        return "ERRO_NAO_LANCADO"
    except AttributeError:
        return "ERRO_ESPERADO"
    except Exception as e:
        return f"ERRO_TIPO_ERRADO: {type(e).__name__}"

CMDS = {
    "ok": cmd_ok,
    "set_ok": cmd_set_ok,
    "set_bad_nome": cmd_set_bad_nome,
    "set_bad_preco": cmd_set_bad_preco,
    "email_bad": cmd_email_bad,
    "ctor_bad_nome": cmd_ctor_bad_nome,
    "ctor_bad_preco": cmd_ctor_bad_preco,
    "mangled": cmd_mangled,
    "direct": cmd_direct,
}

if __name__ == "__main__":
    cmd = input().strip()
    if cmd in CMDS:
        print(CMDS[cmd]())
    else:
        print("Comando inválido")
