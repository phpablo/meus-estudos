from src.models.categoria import Categoria
from src.utils.persistencia import Persistencia

class CategoriaController:
    def __init__(self):
        # Carrega do arquivo ao iniciar
        self._categorias = Persistencia.carregar_categorias()

    def criar_categoria(self, nome: str, tipo: str, limite: float = 0.0, descricao: str = ""):
        """
        Cria uma nova categoria e a adiciona à lista, se não houver duplicidade.
        """
        # 1. Sanitização: Limpa espaços e deixa maiúsculo para comparar direito
        nome_ajustado = nome.strip()
        tipo_ajustado = tipo.strip().upper()

        # 2. Regra de Negócio: Impedir duplicidade de nomes no mesmo tipo
        if self._existe_categoria(nome_ajustado, tipo_ajustado):
            raise ValueError(f"Erro: Já existe uma categoria '{nome_ajustado}' do tipo '{tipo_ajustado}'.")

        # 3. Criação do Objeto (Chama o Model)
        nova_categoria = Categoria(nome_ajustado, tipo_ajustado, limite, descricao)

        # 4. Persistência em Memória (Adiciona na lista)
        self._categorias.append(nova_categoria)

        # PERSISTÊNCIA: Salva a lista atualizada no disco
        Persistencia.salvar_categorias(self._categorias)

        return nova_categoria

    def listar_todas(self):
        """Retorna uma cópia da lista de categorias."""
        return self._categorias[:]

    def _existe_categoria(self, nome, tipo):
        """Método auxiliar (privado) para verificar duplicidade."""
        for categoria in self._categorias:
            if categoria.nome.upper() == nome.upper() and categoria.tipo == tipo:
                return True
        return False