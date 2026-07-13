/**
 * Função para calcular o fatorial de um número.
 * Esta função recebe um número como parâmetro e retorna o seu fatorial.
 *
 * @param {number} n - O número para o qual o fatorial será calculado.
 * @returns {number} O fatorial do número especificado.
 */
function fatorial(n) {
  let fat = 1;
  for (let c = n; c > 1; c--) {
    fat *= c;
  }
  return fat;
}

// Exemplo de uso da função para calcular o fatorial de 5
console.log(fatorial(5));
