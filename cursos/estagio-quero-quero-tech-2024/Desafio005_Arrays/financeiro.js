// crias as variaveis necessarias 
// let categorias = ['alimentacao', 'transporte', 'lazer'];f
let categorias = [];
let valor = [];
let media;
let soma = Number(0);
let mediaAlimentacao = Number(0);
let mediaTransporte = Number(0);
let mediaLazer = Number(0);
let gastoAlimentacao = Number(0);
let gastoLazer = Number(0);
let gastoTransporte = Number(0);

/**
 * Função para registros financeiros
 * @returns {string} - Mensagem com os resultados
 */
function rastreadorFinanceiro() {

  // loop para registrar as atividades
  for (let i = 0; i < 3; i++) {

    let msg = parseInt(prompt('Deseja cadastrar uma despesa? \n 1 = SIM \n 2 - NÃO'))
    if (msg == 2) {
      alert('Sessão de registros finalizada')
      break;
    } else {
      let inputCategoria = parseFloat(prompt(`Qual categoria deseja registrar o gasto: \n 1 - Alimentação \n 2 - Transporte \n 3 - Lazer`));

      valor = parseFloat(prompt(`Qual valor gasto: `));

      let categoria;
      if (inputCategoria == 1) {
        categoria = 'Alimentacao';
      } else if (inputCategoria == 2) {
        categoria = 'Transporte';
      } else {
        categoria = 'Lazer';
      }
      categorias.push({ categoria: categoria, valor: valor });
      soma += categorias[i].valor;
    }
  }


  for (let i = 0; i < categorias.length; i++) {

    if (categorias[i].categoria == 'Alimentacao') {
      mediaAlimentacao++;
      gastoAlimentacao += categorias[i].valor;
    } else if (categorias[i].categoria == 'Transporte') {
      mediaTransporte++;
      gastoTransporte += categorias[i].valor;
    } else {
      mediaLazer++;
      gastoLazer += categorias[i].valor;
    }
  }

  mediaAlimentacao = gastoAlimentacao / mediaAlimentacao;
  mediaTransporte = gastoTransporte / mediaTransporte;
  mediaLazer = gastoLazer / mediaLazer;


  console.log(`===Registro de Gastos===`);
  for (let i = 0; i < categorias.length; i++) {

    console.log(`Valor total gasto: R$ ${soma.toFixed(2)} \n Media Alimentacao: R$ ${mediaAlimentacao.toFixed(2)} \n Media Transporte: R$ ${mediaTransporte.toFixed(2)} \n Media Lazer: R$ ${mediaLazer.toFixed(2)}\n=====================`)
  }

  return ''
}

// chama a função 
rastreadorFinanceiro();