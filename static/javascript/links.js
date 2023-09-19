// Obtenha a referência ao elemento select
var select = document.getElementById("tipo__app");

// Adicione um evento onchange
select.addEventListener("change", function () {
    // Obtenha o valor selecionado
    var selectedValue = select.value;

    // Redirecione com base na opção selecionada
    switch (selectedValue) {
        case "Home":
            window.location.href = "/";
            break;
        case "Cadastro":
            window.location.href = "/cadastro";
            break;
        case "Relação":
            window.location.href = "/relacao";
            break;
        case "Siglas de Tag":
            window.location.href = "/sigla";
            break;
        default:
            // Redirecione para uma página padrão, se necessário
            window.location.href = "/login";
    }
});

document.addEventListener("DOMContentLoaded", function () {
    // Seleciona o elemento <select>
    const selectElement = document.getElementById("tipo__app");

    // Verifica a URL atual e define a opção no <select> com base nela
    switch (window.location.pathname) {
        case "/":
            selectElement.value = "Home";
            break;
        case "/cadastro":
            selectElement.value = "Cadastro";
            break;
        case "/relacao":
            selectElement.value = "Relação";
            break;
        case "/sigla":
            selectElement.value = "Siglas de Tag";
            break;
        default:
            // Se a URL não corresponder a nenhuma das opções, você pode deixar a seleção padrão (vazio)
            selectElement.value = "";
    }
});