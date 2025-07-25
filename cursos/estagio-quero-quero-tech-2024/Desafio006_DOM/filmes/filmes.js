const filmes = []
let filmesOrdenados = []


function cadastroFilmes() {
  let nome = document.getElementById('nome').value;
  let nota = document.getElementById('nota').value;

  let filme = {
    nome: nome,
    nota: nota
  }

  filmes.push(filme);
  console.log(nome);
  console.log(nota);
  console.log(filmes);

  let msg = document.getElementById('resultado');
  msg.innerHTML = 'Cadastro realizado com sucesso';


  document.getElementById('nome').value = '';
  document.getElementById('nota').value = '';
  document.getElementById('resultado').value = '';
}

function mostraResultados() {
  if (filmes.length === 0) {

    let resultado = document.getElementById('resultado');
    resultado.innerHTML = '<p>Lista Vazia</p>';

  } else {
    
    filmesOrdenados = filmes.sort((a,b) => b.nota - a.nota);

    for (let i = 0; i < filmesOrdenados.length; i++) {
      let resultado = ''
      resultado = document.getElementById('resultado');
      resultado.innerHTML += `<ul><li>Filme: <strong>${filmesOrdenados[i].nome}</strong> e nota : <strong>${filmesOrdenados[i].nota}</strong>`;
    }

  }

}
