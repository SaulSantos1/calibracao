document.addEventListener("DOMContentLoaded", function() {
    const filtrarButton = document.getElementById("filtrarOrdem");
    filtrarButton.addEventListener("click", function() {
        const select = document.getElementById("ordemproducao");
        const selectedValues = Array.from(select.selectedOptions).map(option => option.value);

        // Seleciona a tabela com o título "Ordem de Produção"
        const tabelaOrdemProducao = document.querySelector(".table:nth-of-type(2)"); // A segunda tabela

        // Seleciona apenas as linhas da tabela "Ordem de Produção"
        const tableRows = tabelaOrdemProducao.querySelectorAll(".table__body tbody tr");
        tableRows.forEach(row => {
            const codigo = row.querySelector("td:first-child").textContent;
            if (selectedValues.length === 0 || selectedValues.includes(codigo)) {
                row.style.display = "table-row";
            } else {
                row.style.display = "none";
            }
        });
    });
});