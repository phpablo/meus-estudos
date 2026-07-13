var idade = 20;
console.log(`Sua idade é ${idade}`);
if (idade < 16) {
  console.log('Não vota');
} else if (idade < 18 || idade >= 65) {
  console.log('Voto Opcional');
}else {
  console.log('Voto Obrigatório');
}