class Categoria:
    def __init__(self,nome:str, tipo:str, limite:float = 0.0, descricao:str = " "):
        self._nome = nome
        self._tipo = tipo.upper()
        self._limite = limite
        self._descricao = descricao
        self.validar_limite()

    @property
    def nome(self):
        return self._nome
    @property
    def tipo(self):
        return self._tipo
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self,valor):
        self._limite = valor
        self.validar_limite()

    def validar_limite(self):
        if self._tipo == "RECEITA" and self._limite > 0:
            print(f"Aviso: O limite foi ajustado para 0, pois a categoria '{self._nome}' é de RECEITA.")
            self._limite = 0.0

    def __str__(self):
        return f"{self._nome} ({self._tipo})"

    def __repr__(self):
        return f"Categoria(nome='{self._nome}', tipo='{self._tipo}', limite={self._limite})"

    # Adicione no final da classe Categoria:
    def to_dict(self):
        return {
            "nome": self._nome,
            "tipo": self._tipo,
            "limite": self._limite,
            "descricao": self._descricao
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(dados['nome'], dados['tipo'], dados['limite'], dados['descricao'])

