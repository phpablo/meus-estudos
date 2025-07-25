/**
 * Desafio 002 - Fibonacci
 * Gera sequencia informada pelo usuario
 */

// pego o valor inputado pelo usuario
const N = parseInt(prompt('Digite qual o tamanho da sequencia de fibonnacci será gerada: '));

// crio um array ja com o valores no indice 0 e 1
let fibo =[0,1];

// funcao para gerar a sequencia
function gerarSequencia(N) {
    if(N <=0){
        // se igual ou menor que zero, não tem como gerar 
        console.log("[ DIGITE UM NÚMERO VÁLIDO]");
    }else if ( N === 1) {
        
        // se for igual a 1, retorna so o valor do primeiro indice
        console.log(fibo[0]);
    }else {
        // se for maior que 1, gerar a sequencia num laço de repetição
        for(i = 2; i < N; i++) {
            fibo[i] = fibo[i-1] + fibo[i-2];
        }
    // imprime o array
    console.log(fibo);
    }
}
// chama a função para ser executada.
gerarSequencia(N);