/**
 * Função para gerar CPF
 * 
 * @param {number} [min=0]
 * @param {number} [max=9]
 * @return {*} 
 */
function geradorCPF(min = 0, max = 9) {

  let cpf = '';
  for (let i = 1; i <= 9; i++) {
    
    min = Math.ceil(min);
    max = Math.floor(max);
    if(i == 3 || i== 6) {
      cpf += Math.floor(Math.random() * (max - min + 1)) + min +'.';
    }else {
      cpf += Math.floor(Math.random() * (max - min + 1)) + min;
    }
  }

  return console.log(cpf);
}
// chamada da função 
geradorCPF();