/**
 * Calcula e exibe uma mensagem sobre multa devido ao excesso de peso de peixes.
 * @param {number} pesoPeixe - Peso do peixe em quilogramas.
 * @return {void} Não retorna valor, mas exibe uma mensagem no console.
 */

// solicita ao usuario a matrícula e adiciona na variavel C
let c = parseInt(prompt('Qual sua matrícula ? '));

// solicita ao usuario o número de horas trabalhadas e adiciona na variavel N
let n = parseFloat(prompt('Quantas horas trabalhadas: '));

// inicializa uma variavel E de Valor/horas excedidas iniciando em zero
let e = Number(0);

// valor hora fixo
const VALOR_HORA = Number(10);
const VALOR_HORA_EXCEDENTE = Number(20);


if(n > 50) {

  e = (n - 50) * VALOR_HORA_EXCEDENTE;
  salario = 50 * VALOR_HORA;
  salario = salario + e;
  console.log('Valor do Salário Total: R$ ' + salario);
  console.log('Valor do Salário Excedente : R$  ' + e);
}else {
  salario = n * VALOR_HORA;
  console.log('Valor Salário: R$' + salario);
  console.log('Valor Excedente: R$ 0,00');

}

