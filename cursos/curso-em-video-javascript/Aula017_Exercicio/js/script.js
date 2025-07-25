/**
 * Função para contar de acordo com os parâmetros fornecidos pelo usuário.
 */
function contar() {
  // Obtém os elementos HTML dos campos de entrada e resultado
  let ini = document.getElementById('txti');
  let fim = document.getElementById('txtf');
  let pas = document.getElementById('txtp');
  let res = document.getElementById('res');

  let p = Number(pas.value);
  if ( p <=0) {
    window.alert('Passo inválido, considerando passo 1');
    p = 1;
    pas.value = p;
  }

  // Verifica se todos os campos foram preenchidos
  if (ini.value.length == 0 || fim.value.length == 0 || pas.value.length == 0) {
    // Se algum campo estiver vazio, exibe um alerta de erro
    alert('[ERRO] Faltam dados!');
  } else {
    // Caso contrário, realiza a contagem
    res.innerHTML = 'Contando...<br>';

    // Converte os valores dos campos de entrada para números
    let i = Number(ini.value);
    let f = Number(fim.value);
    let p = Number(pas.value);

    // Verifica se a contagem é ascendente ou descendente
    if (i < f) {
      // Se for ascendente, realiza a contagem ascendente e exibe os resultados
      for (let c = i; c <= f; c += p) {
        res.innerHTML += `${c} \u{1F449}`;
      }
    } else {
      // Se for descendente, realiza a contagem descendente e exibe os resultados
      for (let c = i; c >= f; c -= p) {
        res.innerHTML += `${c} \u{1F449}`;
      }
    }
    // Adiciona um emoji de bandeira de chegada para indicar o fim da contagem
    res.innerHTML += `\u{1F3C1}`;
  }
}