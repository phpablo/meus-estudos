/**
 * Calcula o fatorial de um número.
 * @param {number} n - O número para o qual calcular o fatorial.
 * @returns {number} - O fatorial de `n`.
 */
function fatorial(n) {
  // Verifica se `n` é igual a 1, pois o fatorial de 1 é 1.
  if (n == 1) {
    return 1;
  } else {
    // Se `n` não for igual a 1, calcula o fatorial de `n` multiplicando `n` pelo fatorial de (n-1).
    return n * fatorial(n - 1);
  }
}

// Exemplo de uso: Calcula o fatorial de 5 e exibe o resultado no console.
console.log(fatorial(5)); // Saída: 120
