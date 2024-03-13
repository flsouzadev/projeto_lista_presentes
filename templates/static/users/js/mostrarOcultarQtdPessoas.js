function mostrarFormularioPresente() {
    var checkbox1 = document.getElementById('checkbox1');
    var checkbox2 = document.getElementById('checkbox2');
    var formularioQuantidadePessoas = document.getElementById('formularioQuantidadePessoas');
    var formularioInfoPessoais = document.getElementById('formularioInfoPessoais');
    
    if (checkbox1.checked) {
      formularioQuantidadePessoas.style.display = 'block';
      checkbox2.checked = false; // Desmarca o checkbox2
      formularioInfoPessoais.style.display = 'none'; // Esconde o formulárioInfoPessoais
    } else {
      formularioQuantidadePessoas.style.display = 'none';
    }
  }

  function mostrarFormularioAusente() {
    var checkbox1 = document.getElementById('checkbox1');
    var checkbox2 = document.getElementById('checkbox2');
    var formularioQuantidadePessoas = document.getElementById('formularioQuantidadePessoas');
    var formularioInfoPessoais = document.getElementById('formularioInfoPessoais');
    
    if (checkbox2.checked) {
      formularioInfoPessoais.style.display = 'block';
      checkbox1.checked = false; // Desmarca o checkbox1
      formularioQuantidadePessoas.style.display = 'none'; // Esconde o formularioQuantidadePessoas
      document.getElementById('listaItens').style.display = 'none';
    } else {
      formularioInfoPessoais.style.display = 'none';
    }
  }

  function mostrarOcultarFormulario() {
    var checkbox = document.getElementById('mostrarFormulario');
    var formulario = document.getElementById('formularioContato');
    
    if (checkbox.checked) {
        formulario.style.display = 'block';
    } else {
        formulario.style.display = 'none';
    }
}

  //   // Vincula a função ao evento de clique do botão
  // document.getElementById('acessarLista').addEventListener('click', mostraFormularioLista);

  // // Define a função que será chamada quando o botão for clicado
  // function mostraFormularioLista() {
  //   var formulario = document.getElementById("formularioLista");

  //   // Alterna entre mostrar e ocultar o formulário
  //   if(formulario.style.display === 'none') {
  //     formulario.style.display = 'block';
  //   } else {
  //     formulario.style.display = 'none';
  //   }
  // }
