let senha = prompt('Digite uma senha: ');
let forcaSenha = 0;
let resultados = '';

/**
 * Analisa a senha e define sua força
 *
 * @param {string} senha - Senha digitada pelo usuario
 * @return {string} - Mensagem com resultado 
 */
function analisaSenha (senha) {

  // verifica se tem 8 caracteres no minimo 
  if(senha.length >= 8) {
    forcaSenha++;
  }

  // verifica se possui letra maiúscula 
  if(/[A-Z]/.test(senha)) {
    forcaSenha++;
  }

  // verifica se tem letra minúscula 
  if(/[a-z]/.test(senha)) {
    forcaSenha++;
  }

  // verifica se tem um número 
  if(/\d/.test(senha)) {
    forcaSenha++;
  }

  // verifica se possui caracter especial 
  if(/[@#$%]/.test(senha)) {
    forcaSenha++;
  }

  // classifica a senha pela força incrementada 
  if(forcaSenha == 5) {
    resultados = console.log('Senha Forte\n Possui minimo de 8 caracteres \n Uma Letra maiúscula \n Uma letra minuscula \n Um número \n Um caracter especial');
  }

  if(forcaSenha == 4 || forcaSenha == 3) {
    resultados = console.log('Senha Media\n Precisa conter um caracter especial e um número');
  }

  if(forcaSenha == 2 || forcaSenha == 1) {
    resultados = console.log('Senha Fraca\n Precisa conter um caracter especial, um número, uma letra maiuscula, uma minuscula e minimo de 8 caracteres');
  }

  return resultados;
}

// chamada da funcao 
analisaSenha(senha);