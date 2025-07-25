let gastos = [];
let gastoTotal = 0;

function cadastraGasto() {

  let categ = document.getElementById('categoria').value;
  let valor = parseFloat(document.getElementById('valor').value);

  let registro = {
    categoria: categ,
    valor: valor
  }

  gastos.push(registro);

  document.getElementById('categoria').value = '';
  document.getElementById('valor').value = '';
  console.log(gastos);
}

function mostraResultados() {
  if (gastos.length === 0) {
    let resultado = document.getElementById('resultado');
    resultado.innerHTML = '<p>Lista Vazia</p>';s
  } else {
    let gastosUnicos = {};

    // Calcula valor total gasto em todas as categorias
    for (let i = 0; i < gastos.length; i++) {
      gastoTotal += gastos[i].valor;
      
      // Registra o tempo gasto em cada atividade
      if (!gastosUnicos[gastos[i].categoria]) {
        gastosUnicos[gastos[i].categoria] = {
          valor: 0,
          quantidade: 0
        };
      }
      gastosUnicos[gastos[i].categoria].valor += gastos[i].valor;
      gastosUnicos[gastos[i].categoria].quantidade++;
    }

    let resultado = document.getElementById('resultado');
    resultado.innerHTML = '';

    // Calcula e exibe a média de tempo gasto em cada atividade
    for (let gasto in gastosUnicos) {
      let mediaGasto = gastosUnicos[gasto].valor / gastosUnicos[gasto].quantidade;
      resultado.innerHTML += `<p>Média de valor gasto em ${gasto}: <strong>${mediaGasto.toFixed(2)}</strong></p>`;

    }

    // Exibe o tempo total gasto em todas as atividades
    resultado.innerHTML += `<p>Gasto total: <strong>${gastoTotal}</strong></p>`;
  }
}