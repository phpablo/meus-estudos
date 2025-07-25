// crias as variaveis necessarias 
let temperatura = [];
let diaSemana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado'];
let tempMedia;
let tempMin = [];
let tempMax = [];
let soma = Number(0);

/**
 * Função para calcular temperatura max,min e media da semana
 * @returns {string} - Mensagem com os resultados
 */
function registraTemperatura() {

  // loop para registrar a temperatura de cada dia 
  for (let i = 0; i < 7; i++) {

    let graus = parseFloat(prompt(`Qual a temperatura máxima de ${diaSemana[i]}`))
    temperatura.push({ dia: diaSemana[i], graus: graus })
  }

  // loop para somar todas as temperaturas
  for (let i = 0; i < temperatura.length; i++) {
    soma += temperatura[i].graus;
  }

  // calcula a media
  tempMedia = soma / 7;

  // ordena por ordem crescente
  tempMin = temperatura.sort((a, b) => a.graus - b.graus);

  // ordena por ordem decrescente
  tempMax = temperatura.sort((a, b) => b.graus - a.graus);

  return console.log(`=== Registro da temperatura semanal ===: \n Média de ${tempMedia.toFixed(2)} graus \n Máxima de ${tempMax[0].graus}\n Mínima de ${tempMin[6].graus}\n----------------------------`)
}

// chama a função 
registraTemperatura();