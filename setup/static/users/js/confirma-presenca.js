function toggleQuantidadePessoas() {
    var checkboxSim = document.getElementById('item1');
    var checkboxNao = document.getElementById('item2');
    var divQuantidadePessoas = document.getElementById('div-quantidade-pessoas');
    var divNomeAusente = document.getElementById('div-nome');
    var botao1 = document.getElementById('botao-1');
    var botao2 = document.getElementById('botao-2');


    if (checkboxSim.checked) {
        divQuantidadePessoas.style.display = 'block';
        botao1.style.display = 'block';
        botao2.style.display = 'none';
        if (divNomeAusente) {
            divNomeAusente.style.display = 'none';
        }
    } else if (checkboxNao.checked) {
        divQuantidadePessoas.style.display = 'none';

        botao1.style.display = 'none';
        botao2.style.display = 'block';

        var quantidadePessoasInput = document.getElementById('quantidade-pessoas');
        var quantidadePessoas = quantidadePessoasInput.value;
        if (quantidadePessoas > 0) {
            quantidadePessoasInput.value = 0;
        }
        document.getElementById('campos-pessoas').innerHTML = '';

        if (!divNomeAusente) {
            var divNomeAusente = document.createElement('div');
            divNomeAusente.id = 'div-nome';
            divNomeAusente.classList.add('mb-3');

            // Cria a label e define o atributo 'for' com o ID do input correspondente
            var labelNomeAusente = document.createElement('label');
            labelNomeAusente.setAttribute('for', 'nome_pessoa');
            labelNomeAusente.textContent = 'Insira seu nome para concluirmos a confirmação';

            // Cria o input e define o ID correspondente
            var inputNomeAusente = document.createElement('input');
            inputNomeAusente.setAttribute('type', 'text');
            inputNomeAusente.setAttribute('id', 'nome_pessoa');
            inputNomeAusente.setAttribute('name', 'nome_pessoa');
            inputNomeAusente.setAttribute('placeholder', 'Seu Nome ');
            inputNomeAusente.classList.add('form-control');
            inputNomeAusente.setAttribute('style', 'margin-top: 10px');

            // Adiciona a label e o input à divNomeAusente
            divNomeAusente.appendChild(labelNomeAusente);
            divNomeAusente.appendChild(inputNomeAusente);

            document.getElementById('campo-pessoas-ausentes').appendChild(divNomeAusente);

            // Insere a divNomeAusente após divQuantidadePessoas
            divQuantidadePessoas.parentNode.insertBefore(divNomeAusente, divQuantidadePessoas.nextSibling);
        } else {
            divNomeAusente.style.display = 'block';
        }
    } else {
        divQuantidadePessoas.style.display = 'none';
        if (divNomeAusente) {
            divNomeAusente.style.display = 'none';
        }
        botao1.style.display = 'none';
        botao2.style.display = 'none';
    }
}

var checkboxes = document.querySelectorAll('input[name="presenca"]');
checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', toggleQuantidadePessoas);
});
