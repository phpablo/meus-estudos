// inicia os arrays vazios
let filmes = new Array();
let nota = new Array();
let filmesOrdenados = [];

/**
 *Função para cadastrar e ordenar baseado na nota
 *
 * @return {string} - Mensagem com o resultado 
 */
function cadastroFilmes() {

  // solitação ao usuario 
  let msg = parseInt(prompt("Deseja Cadastrar um filme: \n 1 - SIM \n 2 - NAO"));

  // opção pro usuario para o cadastro
  if (msg == 2) {

    alert('Fim do cadastro de filmes');
  } else {

    // loop de cadastro de filmes 
    for (i = 0; i < 10; i++) {

      filmes[i] = prompt('Digite o nome do filme:');
      nota[i] = prompt('Dê uma nota de 0 à 5 ao filme: ');
      msg = parseInt(prompt("Deseja Cadastrar um filme: \n 1 - SIM \n 2 - NAO"));

      if (msg == 2) {
        alert('Fim do cadastro de filmes');
        break;
      }

    }
  }

  // loop para criar 1 array com nome e nota dos filmes respectivamente mantendo a relação nome-nota
  for(i=0; i < filmes.length; i++){
    filmesOrdenados.push({nome: filmes[i],nota: nota[i]});
  }

  // ordena os filmes baseado na nota decrescente
  filmesOrdenados.sort((a,b) => b.nota - a.nota);

  // loop para mostrar na tela o resultado final do cadastro
  for(let i = 0; i < filmesOrdenados.length; i++) {
    
    console.log(`Filme: ${filmesOrdenados[i].nome} teve a nota ${filmesOrdenados[i].nota}`);
  }

  return '';

}

// chamada da função
cadastroFilmes();
