/**
 * Função para verificar se um número é par ou ímpar.
 * Esta função recebe um número como parâmetro e retorna uma string indicando se o número é par ou ímpar.
 *
 * @param {number} n - O número a ser verificado.
 * @returns {string} - Uma mensagem indicando se o número é par ou ímpar.
 */

function parImpar(n) {
  if (n % 2 === 0) {
    return '=== É par! ===';
  } else {
    return '=== É ímpar! ===';
  }
}

// Exemplo de uso da função para verificar se o número 4 é par ou ímpar
let resultado = parImpar(4);
console.log(resultado);
