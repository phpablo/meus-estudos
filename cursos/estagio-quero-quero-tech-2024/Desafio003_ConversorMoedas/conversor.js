/** 
 * Implemente um conversor de moedas que converta um valor digitado pelo usuário de Real para Dólar, Euro, ou outra 
 * moedade sua escolha, considerando uma taxa de conversão fixa.
*/

/**
 * Função que converte o valor informado para Dolar,Euro e Iens
 * 
 * @param {float} valor - Input do usuário 
 * @returns {string} - resultados
 */
function conversor(valor) {
  let resultados = '';

  for(let i = 1; i <=3; i++) {
    let moeda;
    let valorConvertido;

    if( i === 1) {
      moeda = 'Dólar';
      valorConvertido = valor * dolar; 
    } else if (i === 2) {
      moeda ='Euro';
      valorConvertido = valor * euro;
    } else {
      moeda = 'Iens';
      valorConvertido = valor * iens;
    }

    resultados += `Valor informado em reais: R$ ${valor}, em ${moeda} será ${valorConvertido}\n`;
  }

  return resultados;
};

// usuario informa o valor desejado
let valor = parseFloat(prompt("Informe um valor : "));

// taxa do dolar 
let dolar = 5;

// taxa do euro 
let euro = 6;

// taxa do iens 
let iens = 7;

console.log(conversor(valor));

