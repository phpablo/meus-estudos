/**
 * Desafio 003 - Raio
 * Calcula área de circulo
 */

// pega o valor do raio digitado pelo usuario
let raio = parseFloat(prompt('Digite o valor do raio: '))

// funcao para calcular o raio
function calcularRaio(raio) {
    // se raio for menor que zero, aparece um alerta na tela e a função retorna -1
    if(raio < 0) {
        console.log('Número inválido! Informar um número igual ou maior que zero');
        return -1;
    }else {
        // se for maior que zero, faz a conta usando a formula de Area = Pi * raio ao quadrado e retorna o valor
        let area = Math.PI * raio **2;
        return area;
    }
}

// adiciona na variavel areaDoCirculo o valor do raio
let areaDoCirculo = calcularRaio(raio);

// imprime no console a mensagem
console.log("Raio digitado foi "+raio+". Área do Circulo é : "+ areaDoCirculo.toFixed(2));


