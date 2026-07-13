// crias as variaveis necessarias 
let tempMin = [];
let tempMax = [];
let dia = [];
let soma = Number(0);
let registro = [];
let registroOrdenados = [];


function cadastraDia() {

  let diaSemana = document.getElementById('dia').value;
  let temperatura = parseFloat(document.getElementById('Temperatura').value);
  
  let dia = {
    dia: diaSemana,
    temperatura: temperatura
  }
  
  registro.push(dia);
  diaSemana = document.getElementById('dia').value = '';
  temperatura = document.getElementById('Temperatura').value = '';

  

  // // loop para registrar a temperatura de cada dia 
  // for (let i = 0; i < 7; i++) {

  //   let graus = parseFloat(prompt(`Qual a temperatura máxima de ${diaSemana[i]}`))
  //   temperatura.push({ dia: diaSemana[i], graus: graus })
  // }

  // // loop para somar todas as temperaturas
  // for (let i = 0; i < temperatura.length; i++) {
  //   soma += temperatura[i].graus;
  // }

  // // calcula a media
  // tempMedia = soma / 7;

  // // ordena por ordem crescente
  // tempMin = temperatura.sort((a, b) => a.graus - b.graus);

  // // ordena por ordem decrescente
  // tempMax = temperatura.sort((a, b) => b.graus - a.graus);

}

function mostraResultados() {
  if (registro.length === 0) {

    let resultado = document.getElementById('resultado');
    resultado.innerHTML = '<p>Lista Vazia</p>';

  } else {
    
    registroOrdenados = registro.sort((a,b) => b.temperatura - a.temperatura);
    tempMax = parseFloat(registroOrdenados[0].temperatura)

    registroOrdenados = registro.sort((a,b) => a.temperatura - b.temperatura);
    tempMin = parseFloat(registroOrdenados[0].temperatura)

    for( let i = 0; i < registroOrdenados.length; i++) {
      soma += registroOrdenados[i].temperatura;
    }
    soma = soma / registroOrdenados.length;
    let resultado = '';
      resultado = document.getElementById('resultado');
      resultado.innerHTML += `Temperatura média <strong>${soma.toFixed(2)}</strong><br> Maior temperatura : <strong>${tempMax}</strong><br>Menor temperatura : <strong>${tempMin}</strong<br>`;
    

  }

}