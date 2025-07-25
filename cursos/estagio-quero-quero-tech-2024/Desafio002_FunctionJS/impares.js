/**
 * Gera os números impares entre os intervalos de 100 e 200.
 */

function criaImpares() {
  
  // Define o intervalo de início e fim
  let min = 100;
  let max = 200;

  // percorre todo o intervalo entre 100 e 200
  for (let c = min; c <= max; c++) {
    // se resto da divisão for diferente de zero, é impar e mostra no console
    if(c % 2 != 0) {
      console.log(c);
    }
  }
}

// chamada para a função
criaImpares();
