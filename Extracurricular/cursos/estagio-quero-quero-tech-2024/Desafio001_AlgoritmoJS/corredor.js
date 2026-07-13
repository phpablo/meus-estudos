/**
 * Desafio 004 - Corredor
 * Calcula velocidade média do corredor
 */

// funcao que vai calcular a velocidade media
function velocidadeMedia (distancia,tempo) {
  // calcula a media dividindo a distancia pelo tempo 
  let media = distancia / tempo;

  // retorna a media
  return media.toFixed(2);
}
// input do usuario da distancia 
let distancia = parseFloat(prompt("Qual distância da maratona em kilômetros ? "));
//input do usuario do tempo q quer fazer a prova
let tempo = parseFloat(prompt("Em quantas horas você quer fazer essa maratona ? "));

// mostra uma mensagem no console.
console.log(`Para correr a maratona de ${distancia} km. Você deve correr em média ${velocidadeMedia(distancia,tempo)} km/h.`);