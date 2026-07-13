function verificar() {
  const data = new Date();
  const ano = data.getFullYear();
  const fano = document.getElementById('ano');
  const res = document.getElementById('res');

  if (fano.value.length === 0 || fano.value > ano) {
    alert('[ERRO] Verifique os dados e tente novamente!')
  } else {

    const fsex = document.getElementsByName('radsex');
    const idade = ano - Number(fano.value);
    var genero = '';
    var img = document.createElement('img');
    img.setAttribute('id', 'foto');

    //Verifica o gênero
    if (fsex[0].checked) {
      genero = 'Homem';
      if (idade >= 0 && idade < 10) {
        
        // criança
        img.setAttribute('src', 'imagens/bb-m.jpg');
      } else if (idade < 21) {
        
        // jovem
        img.setAttribute('src', 'imagens/jovem-m.jpg');
      } else if (idade < 50) {
        
        //adulto
        img.setAttribute('src', 'imagens/adulto-m.jpg');
      } else {
        
        //idoso
        img.setAttribute('src', 'imagens/idoso-m.jpg');
      }
    }
    else if (fsex[1].checked) {
      genero = 'Mulher';
      if (idade >= 0 && idade < 10) {

        // criança
        img.setAttribute('src', 'imagens/bb-f.jpg');
      } else if (idade < 21) {
        
        // jovem
        img.setAttribute('src', 'imagens/jovem-f.jpg');
      } else if (idade < 50) {
        
        //adulto
        img.setAttribute('src', 'imagens/adulto-f.jpg');
      } else {
        
        //idoso
        img.setAttribute('src', 'imagens/idoso-f.jpg');
      }

    }
    res.style.textAlign = 'center';
    res.innerHTML = `Foi detectado ${genero} de ${idade} anos`;
    res.appendChild(img);
  }
}