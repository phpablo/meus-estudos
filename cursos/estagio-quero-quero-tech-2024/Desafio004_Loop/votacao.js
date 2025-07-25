//Implemente um simulador de votação para três candidatos e, após a votação, exiba o resultado

// Pede o usuario para digitar uma opção
let voto = Number(prompt("===== Votação===\n Digite 1 para votar no candidato Pedro. \n Digite 2 para votar no candidato Alvares. \n Digite 3 para votar no candidato Cabral.\n Digite 0 para finalizar a votação!"));

// Declara variaveis para contar votos
let votosPedro   = 0;
let votosAlvares = 0;
let votosCabral = 0;

/**
 * Função para mostrar o resultado da votação
 * 
 * @return {string}  - Mensagem do resultado
 */
function resultadoVotação() {
  // Verifica se o voto digitado pelo usuário é diferente de zero
  if (voto !== 0) {

    // Loop que executa apenas uma vez para processar o voto do usuário
    for (let i = 0; i < 1; i++) {
  
      // Verifica em qual candidato o usuário votou e incrementa o contador de votos correspondente
      if (voto === 1) {
        votosPedro++;
      } else if (voto === 2) {
        votosAlvares++;
      } else {
        votosCabral++;
      }
    }
  }

  // retorna mensagem com resultado
  return console.log(`==Votação Finalizada=== \n Pedro teve ${votosPedro} votos.\n Alvares teve ${votosAlvares} votos\n Cabral teve ${votosCabral} votos.`);
}

// chamada da função
resultadoVotação();
