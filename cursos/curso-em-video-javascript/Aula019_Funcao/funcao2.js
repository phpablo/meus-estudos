/**
 * Função para realizar a soma de dois números.
 * Esta função recebe dois números como parâmetros e retorna a soma deles.
 * Se nenhum valor for fornecido, assume-se que os valores padrão são zero.
 *
 * @param {number} n1 - O primeiro número a ser somado (padrão: 0).
 * @param {number} n2 - O segundo número a ser somado (padrão: 0).
 * @returns {number} A soma dos dois números.
 */

function somar(n1 = 0, n2 = 0) {
  return n1 + n2;
}

// Exemplo de uso da função para realizar uma soma e exibir o resultado
console.log('SOMADOR DE NÚMEROS');
console.log('------------------------');
console.log('Resultado da soma:'+ somar(3, 1));
console.log('------------------------');
