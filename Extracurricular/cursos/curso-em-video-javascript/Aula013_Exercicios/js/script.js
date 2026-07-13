function carregar() {
  var msg = window.document.getElementById('msg');
  var img = window.document.getElementById('imagem');
  var data = new Date();
  // var hora = data.getHours();
  // var hora = 9;
  // var hora = 13;
  var hora = 19;

  msg.innerHTML = `Agora são ${hora} horas.`;

  if(hora >=0 && hora < 12) {
    // BOM DIA
    img.src = 'imagens/manha.png';
    document.body.style.background = '#c0cdc8';
  }else if( hora >=12 && hora < 18){
    // BOA TARDE
    img.src = 'imagens/tarde.png';
    document.body.style.background = '#e7bb59';
  }else{
    // BOA NOITE
    img.src = 'imagens/noite.png';
    document.body.style.background = '#11202c';
  }
}