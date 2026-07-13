function geraLimite() {
  let divResultado = document.getElementById('resultado');

  divResultado.style.display = 'block';
  inputUser = document.getElementById('input').value = '';
  let resultado = document.getElementById('resultado');

  resultado.innerHTML += '<p id="mensagemLimite" style="color:red;"> <strong>Putz, você errou 5 vezes</strong> Limite de tentativas atingido<br>Tente novamente!</p>';
  resultado.innerHTML += '<p style="color: #fff;"> O alvo era <strong>'+ alvo +'</strong></p>';

  let btnStart = document.getElementById('start');
  let btnPlay = document.getElementById('play');
  let btnTentar = document.getElementById('tentar');

  btnStart.style.display = 'none';
  btnPlay.style.display = 'none';
  btnTentar.style.display = 'block';
  
  // Define um atraso de 1000 milissegundos (1 segundo) para chamar a função removerMensagem
  // setTimeout(function () {
  //   removerMensagem();
  // }, 5000);
}

function removerMensagem() {

  let mensagemErro = document.getElementById('mensagemLimite');

  if (mensagemErro) {
    mensagemErro.remove();
  }

  let divResultado = document.getElementById('resultado');
  
  divResultado.style.display = 'none';
}
