let atividades = [];
let tempoTotal = 0;
let registraAtividade = [];
let registraTempo = [];


function rastreadorRotina() {


  let atividade = document.getElementById('atividade').value;
  let tempo = parseFloat(document.getElementById('tempo').value);

  let registro = {
    atividade: atividade,
    tempo: tempo
  }

  atividades.push(registro);
  console.log(atividades);
  atividade = document.getElementById('atividade').value = '';
  tempo = document.getElementById('tempo').value = '';

}

function mostraResultados() {
  if (atividades.length === 0) {
    let resultado = document.getElementById('resultado');
    resultado.innerHTML = '<p>Lista Vazia</p>';
  } else {
    let atividadesUnicas = {};

    // Calcula o tempo total gasto em todas as atividades
    for (let i = 0; i < atividades.length; i++) {
      tempoTotal += atividades[i].tempo;
      // Registra o tempo gasto em cada atividade
      if (!atividadesUnicas[atividades[i].atividade]) {
        atividadesUnicas[atividades[i].atividade] = {
          tempo: 0,
          quantidade: 0
        };
      }
      atividadesUnicas[atividades[i].atividade].tempo += atividades[i].tempo;
      atividadesUnicas[atividades[i].atividade].quantidade++;
    }

    let resultado = document.getElementById('resultado');
    resultado.innerHTML = '';

    // Calcula e exibe a média de tempo gasto em cada atividade
    for (let atividade in atividadesUnicas) {
      let mediaTempo = atividadesUnicas[atividade].tempo / atividadesUnicas[atividade].quantidade;
      resultado.innerHTML += `<p>Média de tempo gasto em ${atividade}: <strong>${mediaTempo.toFixed(2)}</strong></p>`;
    }

    // Exibe o tempo total gasto em todas as atividades
    resultado.innerHTML += `<p>Tempo total em atividades: <strong>${tempoTotal}</strong></p>`;
  }
}