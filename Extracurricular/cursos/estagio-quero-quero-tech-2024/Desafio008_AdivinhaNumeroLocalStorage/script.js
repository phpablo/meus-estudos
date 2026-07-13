let palpites = [];
const min = 1;
const max = 100;
let tentativas = 0;
let alvo;

function startGame() {

  removerMensagem();

  tentativas = 0;
  palpites = [];
  alvo = geraAlvo(min, max);

  let btnTentar = document.getElementById('tentar');
  let denovo = document.getElementById('denovo');
  let btnStart = document.getElementById('start');
  let btnPlay = document.getElementById('play');
  let btnRank = document.getElementById('rank');
  let inputNumber = document.getElementById('input');
  let btnNameUser = document.getElementById('nameUser');
  let labelNameUser = document.getElementById('id_nameUser');

  btnTentar.style.display = 'none';
  btnRank.style.display = 'block';
  btnStart.style.display = 'none';
  denovo.style.display = 'none';
  btnPlay.style.display = 'block';
  inputNumber.style.display = 'block';
  btnNameUser.style.display = 'block';
  labelNameUser.style.display = 'block';

}

function jogar() {

  let inputUser = parseInt(document.getElementById('input').value);
  let nameUser = document.getElementById('nameUser').value;

  if (isNaN(inputUser) || inputUser == null || inputUser < 1 || inputUser > 100) {
    
    let error = geraErro()
    
    return error;

  } else {

    if (palpites.length >= 5) {

      let limite = geraLimite();

      return limite;

    } else {

      let registro = {
        nome: nameUser,
        numero: inputUser
      }

      palpites.push(registro);

      console.log('input user:', inputUser);
      console.log("Alvo gerado: ", alvo);
      console.log('Palpite Digitado:', palpites);
    }

    geraDicas();
  }

}

function salvarRankingLocal() {
  
  let btnRank = document.getElementById('rank');
  let btnMostraRank = document.getElementById('mostraRank');

  btnRank.style.display = 'none';
  btnMostraRank.style.display = 'block';

  // Verifica se há dados no ranking
  if (palpites.length > 0) {
    // Obtém o rankingSalvo do Local Storage, se existir
    let rankingSalvo = JSON.parse(localStorage.getItem('rankingSalvo')) || [];
    
    // Cria um objeto para contar as tentativas de cada jogador nesta rodada
    let contadorTentativas = {};

    palpites.forEach(jogador => {
      // Verifica se o jogador já existe no contador de tentativas
      if (contadorTentativas.hasOwnProperty(jogador.nome)) {
        contadorTentativas[jogador.nome]++;
      } else {
        contadorTentativas[jogador.nome] = 1;
      }
    });

    // Atualiza o rankingSalvo com os dados corretos de tentativas para cada jogador nesta rodada
    for (const nomeJogador in contadorTentativas) {
      const jogadorExistente = rankingSalvo.find(jogador => jogador.nome === nomeJogador);
      if (jogadorExistente) {
        jogadorExistente.tentativas += contadorTentativas[nomeJogador];
      } else {
        rankingSalvo.push({ nome: nomeJogador, tentativas: contadorTentativas[nomeJogador] });
      }
    }

    // Ordena o rankingSalvo por ordem crescente de tentativas
    rankingSalvo.sort((a, b) => a.tentativas - b.tentativas);

    // Salva no Local Storage como string
    localStorage.setItem('rankingSalvo', JSON.stringify(rankingSalvo));
    console.log('Ranking salvo no Local Storage:', rankingSalvo);
  } else {
    console.log('Nenhum dado para salvar no ranking.');
  }
}




function mostrarRanking() {
  let rankingSalvo = JSON.parse(localStorage.getItem('rankingSalvo'));
  if (rankingSalvo) {
    // Ordena o rankingSalvo por ordem crescente de tentativas
    rankingSalvo.sort((a, b) => a.tentativas - b.tentativas);

    let rankingHTML = '<h2>Ranking Salvo:</h2><ol>';
    rankingSalvo.forEach((jogador, index) => {
      rankingHTML += `<li>${index + 1}º - ${jogador.nome} - ${jogador.tentativas} tentativas</li>`;
    });
    rankingHTML += '</ol>';

    document.getElementById('resultado').innerHTML = rankingHTML;
    document.getElementById('resultado').style.display = 'block';
  } else {
    alert('Ainda não há ranking salvo.');
  }
}





function geraAlvo(min, max) {

  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);

  return Math.floor(Math.random() * (maxFloored - minCeiled + 1) + minCeiled);
}

