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
  let inputNumber = document.getElementById('input');

  btnTentar.style.display = 'none';
  btnStart.style.display = 'none';
  denovo.style.display = 'none';
  btnPlay.style.display = 'block';
  inputNumber.style.display = 'block';

}

function jogar() {

  let inputUser = parseInt(document.getElementById('input').value);

  if (isNaN(inputUser) || inputUser == null || inputUser < 1 || inputUser > 100) {
    
    let error = geraErro()
    
    return error;

  } else {

    if (palpites.length >= 5) {

      let limite = geraLimite();

      return limite;

    } else {

      let registro = {
        numero: inputUser,
      }

      palpites.push(registro);

      console.log('input user:', inputUser);
      console.log("Alvo gerado: ", alvo);
      console.log('Palpite Digitado:', palpites);
    }

    geraDicas();
  }

}


function geraAlvo(min, max) {

  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);

  return Math.floor(Math.random() * (maxFloored - minCeiled + 1) + minCeiled);
}