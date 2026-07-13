/**
 * Função para calcular e exibir a nota do aluno.
 * Esta função recebe a pontuação do aluno como parâmetro e retorna uma mensagem
 * informando a nota obtida pelo aluno.
 *
 * @param {number} n - A pontuação do aluno.
 * @returns {string} - A mensagem contendo a nota do aluno.
 */

let nota = function(n) {
  return 'Sua nota é: ' + n + ' pontos';
}

// Exemplo de uso da função para calcular a nota e exibir a mensagem
console.log(nota(10));
