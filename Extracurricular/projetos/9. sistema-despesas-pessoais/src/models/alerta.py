from datetime import datetime


class Alerta:
    def __init__(self, mensagem: str, categoria_nome: str = None):
        self.mensagem = mensagem
        self.categoria_nome = categoria_nome
        self.data = datetime.now()
        self.visto = False

    def __str__(self):
        return f"[ALERTA ⚠️] {self.data.strftime('%d/%m %H:%M')} - {self.mensagem}"

    def __repr__(self):
        return f"Alerta(msg='{self.mensagem}', cat='{self.categoria_nome}')"