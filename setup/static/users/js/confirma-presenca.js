// document.getElementById('checkbox1').addEventListener('change', function() {
//   if (this.checked) {
//       // Checkbox 1 está marcado, desmarcar checkbox2
//       document.getElementById('checkbox2').checked = false;

//       // Criar ou mostrar o botão especificamente para o checkbox 1
//       var buttonContainer = document.getElementById('buttonContainer');
//       buttonContainer.innerHTML = '<button id="button1">Botão para Checkbox 1</button>';

//       // Criar ou mostrar o input para dados numéricos
//       var inputContainer = document.getElementById('inputContainer');
//       inputContainer.innerHTML = '<input type="number" id="numericInput1" placeholder="Insira um número">';
//   } else {
//       // Checkbox 1 não está marcado
//       // Remover o botão e o input
//       var buttonContainer = document.getElementById('buttonContainer');
//       buttonContainer.innerHTML = '';

//       var inputContainer = document.getElementById('inputContainer');
//       inputContainer.innerHTML = '';
//   }
// });

// document.getElementById('checkbox2').addEventListener('change', function() {
//   if (this.checked) {
//       // Checkbox 2 está marcado, desmarcar checkbox1
//       document.getElementById('checkbox1').checked = false;

//       // Criar ou habilitar o botão especificamente para o checkbox 2
//       var buttonContainer = document.getElementById('buttonContainer');
//       var button2 = document.getElementById('button2');
//       if (button2) {
//           button2.disabled = false;
//       } else {
//           buttonContainer.innerHTML += '<button id="button2" disabled>Botão para Checkbox 2</button>';
//       }

//       // Criar ou mostrar os inputs para nome e RG
//       var inputContainer = document.getElementById('inputContainer');
//       inputContainer.innerHTML = '<input type="text" id="nameInput" placeholder="Nome">' +
//                                   '<input type="text" id="rgInput" placeholder="RG">';
//         document.getElementById('listaItens').style.display = 'none';
//   } else {
//       // Checkbox 2 não está marcado
//       // Desabilitar o botão e remover os inputs
//       var button2 = document.getElementById('button2');
//       if (button2) {
//           button2.disabled = true;
//       }

//       var inputContainer = document.getElementById('inputContainer');
//       inputContainer.innerHTML = '';
//   }
// });