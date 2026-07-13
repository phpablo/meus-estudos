function geraErro() {
  let divResultado = document.getElementById('resultado');

  divResultado.style.display = 'block';
  inputUser = document.getElementById('input').value = '';
  inputUser = document.getElementById('input').value = '';

  let resultado = document.getElementById('resultado');

  resultado.innerHTML += '<p id="mensagemErro" style="color:red;"> <strong>ERRO!</strong> Digite um número entre 1 e 100!</p>';

  // Define um atraso de 1000 milissegundos (1 segundo) para chamar a função removerMensagem
  setTimeout(function () {
    removerMensagem();
  }, 2000);
}
function removerMensagem() {
  let mensagemErro = document.getElementById('mensagemErro');

  if (mensagemErro) {
    mensagemErro.remove();
  }
  
  let divResultado = document.getElementById('resultado');
  divResultado.style.display = 'none';
}
