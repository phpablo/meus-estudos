/**
 * Função para calcular gorjetas
 * @returns {string} - Mensagem com produtos categorizados 
 */
function calculaConta() {
  let valorConta = parseInt(prompt('Qual valor total da sua conta: '));
  let resultado = '';

  // verificar se a quantidade informada é valida 
  if (valorConta >= 1) {


    let qualidadeServiço = parseInt(prompt('Qual sua satisfação com o serviço: \n 1 - Excelente \n 2 - Bom \n 3 - Medio \n 4 - Ruim'));

    // roda o loop 1 vez
    for (let i = 0; i <= 1; i++) {

      let gorjeta = 0;
      let totalConta;

      // classifica a qualidade do serviço e soma a conta total incluindo gorjeta
      if (qualidadeServiço == 1) {

        gorjeta = valorConta * 0.20;
        totalConta = valorConta + (valorConta * 0.20);
        resultado = `===Serviço Excelente=== \n Valor da Conta : R$ ${valorConta} \n Gorjeta de 20% = R$ ${gorjeta} \n Total da Conta R$ ${totalConta} \n ---------------------`;

      } else if (qualidadeServiço == 2) {

        gorjeta = valorConta * 0.15;
        totalConta = valorConta + (valorConta * 0.15);
        resultado = `=== Serviço Bom === \n Valor da Conta : R$ ${valorConta} \n Gorjeta de 15% = R$ ${gorjeta} \n Total da Conta R$ ${totalConta} \n ---------------------`;

      } else if (qualidadeServiço == 3) {

        gorjeta = valorConta * 0.10;
        totalConta = valorConta + (valorConta * 0.10)
        resultado = `=== Serviço Medio === \n Valor da Conta : R$ ${valorConta} \n Gorjeta de 10% = R$ ${gorjeta} \n Total da Conta R$ ${totalConta} \n ---------------------`;
      } else if (qualidadeServiço == 4) {

        gorjeta = valorConta * 0.05;
        totalConta = valorConta + (valorConta * 0.05);
        resultado = `=== Serviço Ruim === \n Valor da Conta : R$ ${valorConta} \n Gorjeta de 5% = R$ ${gorjeta} \n Total da Conta R$ ${totalConta} \n ---------------------`;
      }
    }
  } else {

    // caso quantidade informada incorreta, retorna mensagem de erro e chama novamente a função 
    alert('=== ERRO === \n Valor da conta informado inválida \n Informe uma quantidade maior que zero!')

    // chamada da função 
    calculaConta();
  }

  return console.log(resultado);
}

// chamada da funçãos
calculaConta();
