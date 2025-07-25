/**
 * Calcula e exibe uma mensagem sobre multa devido ao excesso de peso de peixes.
 * @param {number} pesoPeixe - Peso do peixe em quilogramas.
 * @return {void} Não retorna valor, mas exibe uma mensagem no console.
 */

function calculaMulta(p) {
  
  // define o valor do peso permitido 
  let pesoPermitido = parseFloat(50);
  
  // inicializa a variavel de multa zerada 
  let m = parseFloat(0);

  // inicializa a variavel de multa zerada 
  let e = parseFloat(0);

  // verifica se o peso é válido sendo maior que zero 
  if (pesoPeixe <= 0) {
    console.log("Peso inválido! Informe um peso maior do que Zero!");
  } else {
    // condição para peixe está dentro do peso permitido
    if (p <= pesoPermitido) {
      console.log(`O peixe pesa ${pesoPeixe}kg e está dentro do limite de ${pesoPermitido}kg do estado de São Paulo. Peso Excedente: ${e}kg. Valor da Multa: R$ ${m} reais`);
    } else {

      // calcula o peso excedido
      e = pesoPeixe - pesoPermitido;

      // calcula a multa sobre o peso excedido
      m = e * 4;
      console.log(`ATENÇÃO! O peixe pesa ${pesoPeixe}kg, excedendo o limite de ${pesoPermitido}kg permitido em ${e}kg. Isso irá gerar uma multa de R$ 4,00 reais por quilo excedido. Valor da multa: R$ ${m} reais!`);
    }
  }
}

// solicita ao usuario o peso do peixe 
let pesoPeixe = parseFloat(prompt('Qual o peso do peixe? '));
// chamada da função
calculaMulta(pesoPeixe);