  // document.getElementById('qtdPessoas').addEventListener('change', function() {
  //   var quantidadePessoas = parseInt(this.value);

  //   // Limpa os campos anteriores
  //   document.getElementById('campos-pessoas').innerHTML = '';

  //   // Verifica se a quantidade de pessoas é negativa e ajusta para zero
  //   if (quantidadePessoas < 0) {
  //     quantidadePessoas = 0;
  //     this.value = quantidadePessoas; // Atualiza o valor do campo
  //   }

  //   // Cria os campos de nome e RG para cada pessoa
  //   for (var i = 1; i <= quantidadePessoas; i++) {
  //     var divPessoa = document.createElement('div');
  //     divPessoa.classList.add('row', 'pessoa', 'mb-3');

  //     // Adiciona os campos de nome e RG lado a lado usando classes Bootstrap
  //     var inputNomeDiv = document.createElement('div');
  //     inputNomeDiv.classList.add('col');
  //     var inputNome = document.createElement('input');
  //     inputNome.setAttribute('type', 'text');
  //     inputNome.setAttribute('name', 'nome_pessoa_' + i);
  //     inputNome.setAttribute('placeholder', 'Nome da Pessoa ' + i);
  //     inputNome.setAttribute('required', 'required'); // torna o campo obrigatório
  //     inputNome.setAttribute('id', 'nomePresente'); // Define o id para o input
  //     inputNome.classList.add('form-control');
  //     inputNomeDiv.appendChild(inputNome);

  //     var inputRgDiv = document.createElement('div');
  //     inputRgDiv.classList.add('col');
  //     var inputRg = document.createElement('input');
  //     inputRg.setAttribute('type', 'number');
  //     inputRg.setAttribute('name', 'rg_pessoa_' + i);
  //     inputRg.setAttribute('placeholder', 'RG da Pessoa ' + i);
  //     inputRg.setAttribute('required', 'required'); // torna o campo obrigatório
  //     inputRg.setAttribute('id', 'rgPresente'); // torna o campo obrigatório
  //     inputRg.classList.add('form-control');
  //     inputRgDiv.appendChild(inputRg);

  //     divPessoa.appendChild(inputNomeDiv);
  //     divPessoa.appendChild(inputRgDiv);

  //     document.getElementById('campos-pessoas').appendChild(divPessoa);
  //   }
  // });

  // document.getElementById('qtdPessoas').addEventListener('change', function() {
  //   var quantidadePessoas = parseInt(this.value);
  
  //   // Limpa os campos anteriores
  //   document.getElementById('campos-pessoas').innerHTML = '';
  
  //   // Verifica se a quantidade de pessoas é negativa e ajusta para zero
  //   if (quantidadePessoas < 0) {
  //     quantidadePessoas = 0;
  //     this.value = quantidadePessoas; // Atualiza o valor do campo
  //   }
  
  //   // Cria os campos de nome e RG para cada pessoa
  //   for (var i = 1; i <= quantidadePessoas; i++) {
  //     var divPessoa = document.createElement('div');
  //     divPessoa.classList.add('row', 'pessoa', 'mb-3');
  
  //     // Adiciona os campos de nome e RG lado a lado usando classes Bootstrap
  //     var inputNomeDiv = document.createElement('div');
  //     inputNomeDiv.classList.add('col');
  //     var inputNome = document.createElement('input');
  //     inputNome.setAttribute('type', 'text');
  //     inputNome.setAttribute('name', 'nomePresente' + i); // Nome dinâmico
  //     inputNome.setAttribute('placeholder', 'Nome da Pessoa ' + i);
  //     inputNome.setAttribute('id', 'nomePresente' + i); // Id único para cada input de nome
  //     inputNome.setAttribute('class', 'form-control');
  //     inputNomeDiv.appendChild(inputNome);
  
  //     var inputRgDiv = document.createElement('div');
  //     inputRgDiv.classList.add('col');
  //     var inputRg = document.createElement('input');
  //     inputRg.setAttribute('type', 'number');
  //     inputRg.setAttribute('name', 'rgPresente' + i); // Nome dinâmico
  //     inputRg.setAttribute('placeholder', 'RG da Pessoa ' + i);
  //     inputRg.setAttribute('id', 'rgPresente' + i); // Id único para cada input de RG
  //     inputRg.setAttribute('class', 'form-control');
  //     inputRgDiv.appendChild(inputRg);
  
  //     divPessoa.appendChild(inputNomeDiv);
  //     divPessoa.appendChild(inputRgDiv);
  
  //     document.getElementById('campos-pessoas').appendChild(divPessoa);
  //   }
  // });
  
  