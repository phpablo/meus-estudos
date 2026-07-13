document.addEventListener('DOMContentLoaded', () => {
  // Lógica para cada tela específica aqui

  // Exemplo: lógica para cadastro de clientes
  const formCliente = document.getElementById('formCliente');

  formCliente.addEventListener('submit', (e) => {
    e.preventDefault();

    const nomeCliente = document.getElementById('nomeCliente').value.trim();
    // Obter outros campos conforme necessário

    if (nomeCliente !== '') {
      const cliente = {
        nome: nomeCliente,
        // Adicionar outros campos aqui
      };

      salvarCliente(cliente);
      formCliente.reset();
    } else {
      alert('Por favor, preencha todos os campos.');
    }
  });
});

function salvarCliente(cliente) {
  const clientes = JSON.parse(localStorage.getItem('clientes')) || [];
  clientes.push(cliente);
  localStorage.setItem('clientes', JSON.stringify(clientes));
}

// Função de exemplo para mostrar lista de clientes na página
function mostrarClientes() {
  const clientesContainer = document.getElementById('clientesContainer');
  clientesContainer.innerHTML = '';

  const clientes = JSON.parse(localStorage.getItem('clientes')) || [];

  clientes.forEach((cliente, index) => {
    const clienteItem = document.createElement('div');
    clienteItem.textContent = `${index + 1}. ${cliente.nome}`;
    clientesContainer.appendChild(clienteItem);
  });
}

// Adicione a lógica para obter o valor selecionado do datalist
const origemInput = document.getElementById('origem');
const origemList = document.getElementById('origemList');

// Captura o evento de alteração no input para validar a origem selecionada
origemInput.addEventListener('input', function() {
  const selectedOption = origemList.querySelector(`option[value="${origemInput.value}"]`);
  if (selectedOption) {
    console.log('Origem selecionada:', selectedOption.value);
  }
});
