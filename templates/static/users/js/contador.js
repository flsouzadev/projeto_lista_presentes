    // Data do evento (ano, mês - 1, dia, hora, minuto, segundo)
    var dataEvento = new Date('2024-03-23T14:00:00');

    // Atualizar o contador a cada segundo
    setInterval(function() {
        // Data atual
        var dataAtual = new Date();

        // Calcula o tempo restante
        var tempoRestante = dataEvento - dataAtual;

        // Calcula dias, horas, minutos e segundos restantes
        var dias = Math.floor(tempoRestante / (1000 * 60 * 60 * 24));
        var horas = Math.floor((tempoRestante % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutos = Math.floor((tempoRestante % (1000 * 60 * 60)) / (1000 * 60));
        var segundos = Math.floor((tempoRestante % (1000 * 60)) / 1000);

           // Formata o texto com quebras de linha
    var textoFormatado = 'Faltam ' + dias + ' dias<br>' + horas + ' horas<br>' + minutos + ' minutos<br>' + segundos + ' segundos<br>' + 'para o chá de casa nova "Rhe e Victor"';

    // Exibe o contador no elemento HTML
    document.getElementById('contador').innerHTML = textoFormatado;
}, 1000); // Atualiza a cada segundo