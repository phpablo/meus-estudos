let produtos = [];

function cadastrarProduto() {

  let nome = document.getElementById('nome').value;
  let valor = parseFloat(document.getElementById('valor').value); 
  let categoria = document.getElementById('categoria').value;

  let produto = {
    nome: nome,
    valor: valor,
    categoria: categoria
  }

  produtos.push(produto);

  nome = document.getElementById('nome').value = '';
  categoria = document.getElementById('categoria').value = '';
  valor = document.getElementById('valor').value = ''; 
}

function consultarPorCategoria() {
  let categoriaConsulta = document.getElementById('categoriaConsulta').value;
  let produtosFiltrados = produtos.filter(produto => produto.categoria === categoriaConsulta);
  
  exibirResultado(produtosFiltrados);

}

function exibirResultado (produtos) {

  let resultado = document.getElementById('resultado');
  resultado.innerHTML += '';

  if(produtos.length === 0) {
    resultado.innerHTML = '<p> Nenhum produto encontrado</p>';
  }else {
    produtos.forEach(produto => {
      resultado.innerHTML += `<p> Nome: ${produto.nome}, Valor: ${produto.valor.toFixed(2)}, Categoria: ${produto.categoria}</p>`
      
    });
  }
}
