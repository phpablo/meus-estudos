// crias as variaveis necessarias 
let atividades = [];
let diaSemana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado'];
let atividade = ['Corrida', 'Ciclismo', 'Natação'];
let media;
let soma = Number(0);
let mediaCorrida = Number(0);
let tempoCorrida = Number(0);
let mediaCiclismo = Number(0);
let tempoCiclismo = Number(0);
let mediaNatacao = Number(0);
let tempoNatacao = Number(0);

/**
 * Função para rastrear atividades fisicas
 * @returns {string} - Mensagem com os resultados
 */
function rastreadorRotina() {

  // loop para registrar as atividades
  for (let i = 0; i < 7; i++) {

    let atividade = parseFloat(prompt(`Qual a atividade feita ${diaSemana[i]} \n 1 - Corrida \n 2 - Ciclismo \n 3 - Natação`));

    tempo = parseFloat(prompt(`Quantos minutos você fez essa atividade : `));

    let exercicio;
    if (atividade == 1) {
      exercicio = 'Corrida';
    } else if (atividade == 2) {
      exercicio = 'Ciclismo';
    } else {
      exercicio = 'Natação';
    }
    atividades.push({ dia: diaSemana[i], exercicio: exercicio, tempo: tempo })
    soma += atividades[i].tempo;
  }

  for (i = 0; i < atividades.length; i++) {

    if (atividades[i].exercicio == 'Corrida') {
      mediaCorrida++;
      tempoCorrida += atividades[i].tempo;
    } else if (atividades[i].exercicio == 'Ciclismo') {
      mediaCiclismo++;
      tempoCiclismo += atividades[i].tempo;
    } else {
      mediaNatacao++;
      tempoNatacao += atividades[i].tempo;
    }
  }

  mediaCorrida = tempoCorrida / mediaCorrida;
  mediaCiclismo = tempoCiclismo / mediaCiclismo;
  mediaNatacao = tempoNatacao / mediaNatacao;


  console.log(`===Registro de Atividades===`);
  for (i = 0; i < atividades.length; i++) {
    // console.log(`Dia: ${atividades[i].dia} \n Exercicio: ${atividades[i].exercicio} \n Tempo: ${atividades[i].tempo} \n Média da Corrida: ${mediaCorrida} \n Media Ciclismo: ${mediaCiclismo} \n Media Natação: ${mediaNatacao}`);
    console.log(`Tempo total gasto em atividades fisicas: ${soma} \n Media Corrida: ${mediaCorrida} \n Media Ciclismo: ${mediaCiclismo} \n Media Natacao ${mediaNatacao}`)
  }

  return ''
}

// chama a função 
rastreadorRotina();