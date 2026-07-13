// Categoria A: Produtos com preço maior que R$ 1000.

// Categoria B: Produtos com preço entre R$ 501 e R$ 1000.

// Categoria C: Produtos com preço entre R$ 101 e R$ 500.

// Categoria D: Produtos com preço entre R$ 51 e R$ 100.

// Categoria E: Produtos com preço até R$ 50.

// Crie um algoritmo que calcule o preço com desconto de um produto, considerando 
// diferentes faixas de desconto.
// Requisitos do Sistema:
// O sistema deve solicitar ao usuário o número total de produtos que ele deseja classificar.
// Para cada produto, o sistema deve solicitar ao usuário que insira o preço do produto.
// Com base no preço inserido, o sistema deve classificar cada produto em uma das 
// categorias de "A" a "E".
// Após classificação do produto cada, o sistema deve exibir uma categoria correspondente 
// juntamente com o preço do produto.
// Todos os preços e categorias dos produtos devem ser listados ao final da execução do 
// programa

/**
 * Função que categoriza produtos apartir do seu preço
 * @returns {string} - Mensagem com produtos categorizados 
 */
function categorizaProdutos() {
  let qtdProduto = parseInt(prompt('Digite quantos produtos você deseja classificar: '));
  let resultado = '';

  // verificar se a quantidade informada é valida 
  if (qtdProduto >= 1) {

    // itera sobre a quantidade classificando cada produto 
    for (let i = qtdProduto; i >= 1; i--) {

      let produtos = 'Produto: ' + i;
      let msg = Number(prompt('Informe o preço do ' + produtos + '\n'));
      let preco = produtos + ' Preço: R$ ' + msg;
      if (msg > 1000) {
        resultado += '=== Categoria A === \n -> ' + preco + '\n -----------------------\n';
      } else if (msg >= 501) {
        resultado += '=== Categoria B === \n -> ' + preco + '\n -----------------------\n';
      } else if (msg >= 101) {
        resultado += '=== Categoria C === \n -> ' + preco + '\n -----------------------\n';
      } else if (msg >= 51) {
        resultado += '=== Categoria D === \n -> ' + preco + '\n -----------------------\n';
      } else {
        resultado += '=== Categoria D === \n -> ' + preco + '\n -----------------------\n';

      }
    }
  } else {
    // caso quantidade informada incorreta, retorna mensagem de erro e chama novamente a função 
    alert('=== ERRO === \n Quantidade informado inválida \n Informe uma quantidade maior que zero!')

    // chamada da função 
    categorizaProdutos();
  }
  return console.log(resultado);
}

// chamada da funçãos
categorizaProdutos();
