/*
let valores = [2,4,8,6,12];

console.log('==============================');
console.log('Mostrando os valores do array Valores');
for (let pos=0; pos<valores.length; pos++) {
  console.log('- - - - - - - - - - - - - - - - - - - - - - - - ');
  console.log(`A posição ${pos} possui o valor ${valores[pos]}`);
  console.log('- - - - - - - - - - - - - - - - - - - - - - - - ');
}
console.log('==============================');
*/
// @ts-check
let valores = [7,6,2,1,4,3,5];
valores.sort();
console.log(valores);
console.log('===CÓDIGO REFATORADO===');
for(let pos in valores){
  console.log(`Posição: ${pos} | Valor: ${valores[pos]}`);
}
console.log('===FIM DO CÓDIGO===');