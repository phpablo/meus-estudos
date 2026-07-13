// Desenvolva um conversor que transforme um número decimal em binário

/** 
 * Funcao que converte decimal para binario
 * @param {int} - valor digitado pelo usuario
 * @return {string} - mensagem com resultado
*/

// suario digita um valor
let numeroDecimal = parseInt(prompt("Digite um número decimal: "))

function decimalParaBinario(decimal) {

  // Cria variável vazia
  let binario = ""; 

  // Loop para calcular o binário do número decimal
  for (let i = decimal; i > 0; i = parseInt(i / 2)) {
      // Obtém o resto da divisão por 2 (0 ou 1)
      let resto = i % 2;
      // Adiciona o resto na frente da string binária
      binario = resto + binario;
  }

  // Retorna o número binário resultante
  return binario; 
}

// Chama a função
let binarioResultado = decimalParaBinario(numeroDecimal);
console.log(`O número decimal ${numeroDecimal} em binário é: ${binarioResultado}`);
