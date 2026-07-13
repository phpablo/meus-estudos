/**
 * Desafio 001 - Equações de segundo grau
 * Resolve equações do segundo grau usando a fórmula de
 * Bhaskara
 */

function equacaoSegundoGrau(a, b, c) {

  // primeiro eu descubro o delta
  let delta = (b * b) - 4 * a * c;

  // se delta for menor que zero, não tem uma raiz real
  if (delta < 0) {

    console.log("Não possui raiz real");
  } else if (delta === 0) {
    // se delta for igual a zero, tem apenas uma raiz
    let x = -b / (2 * a);
    console.log('Raiz real é:' + x);
  } else {
    // se delta for maior que zero, tem duas raizes, faz o calculo e mostra no console.
    let x1 = (-b + Math.sqrt(delta)) / (2 * a);
    let x2 = (-b - Math.sqrt(delta)) / (2 * a);
    console.log('As raízes são ' + x1 + ' e ' + x2);
  }
}

// solicita o usuário para inputar 3 valores
let a = parseFloat(prompt("Digite o valor de a: "));
let b = parseFloat(prompt("Digite o valor de b: "));
let c = parseFloat(prompt("Digite o valor de c: "));

//chamada da função,passando como parâmetro, os números digitados pelo usuário
equacaoSegundoGrau(a, b, c);
