const search = document.querySelector('.table:first-child .input-group input');
const table_rows = document.querySelectorAll('.table:first-child tbody tr');

search.addEventListener('input',searchTable);

function searchTable(){
    table_rows.forEach((row,i) => {
        let table_data = row.textContent.toLowerCase(),
            search_data = search.value.toLowerCase();

        row.classList.toggle('hide',table_data.indexOf(search_data) < 0);
        row.style.setProperty('--delay', i / 25 + 's')
    })

    document.querySelectorAll('.table:first-child tbody tr:not(.hide)').forEach((visible_row, i) => {
        visible_row.style.backgroundColor = (i % 2 == 0) ? 'transparent' : ''
    }) 
}

const search2 = document.querySelector('.input-group2 input');
const table_rows2 = document.querySelectorAll('.table:nth-child(2) tbody tr');

search2.addEventListener('input', searchTable2);

function searchTable2() {
    table_rows2.forEach((row, i) => {
        let table_data = row.textContent.toLowerCase();
        let search_data = search2.value.toLowerCase();

        row.classList.toggle('hide', table_data.indexOf(search_data) < 0);
        row.style.setProperty('--delay', i / 25 + 's');
    });

    document.querySelectorAll('.table:nth-child(2) tbody tr:not(.hide)').forEach((visible_row, i) => {
        visible_row.style.backgroundColor = i % 2 === 0 ? 'transparent' : '';
    });
}

const search3 = document.querySelector('.input-group3 input');
const table_rows3 = document.querySelectorAll('.table:nth-child(3) tbody tr');

search3.addEventListener('input',searchTable3);

function searchTable3(){
    table_rows3.forEach((row,i) => {
        let table_data = row.textContent.toLowerCase(),
            search_data = search3.value.toLowerCase();

        row.classList.toggle('hide',table_data.indexOf(search_data) < 0);
        row.style.setProperty('--delay', i / 25 + 's')
    })

    document.querySelectorAll('.table:nth-child(3) tbody tr:not(.hide)').forEach((visible_row, i) => {
        visible_row.style.backgroundColor = (i % 2 == 0) ? 'transparent' : ''
    }) 
}

const search4 = document.querySelector('.input-group4 input');
const table_rows4 = document.querySelectorAll('.table:nth-child(4) tbody tr');

search4.addEventListener('input',searchTable4);

function searchTable4(){
    table_rows4.forEach((row,i) => {
        let table_data = row.textContent.toLowerCase(),
            search_data = search4.value.toLowerCase();

        row.classList.toggle('hide',table_data.indexOf(search_data) < 0);
        row.style.setProperty('--delay', i / 25 + 's')
    })

    document.querySelectorAll('.table:nth-child(4) tbody tr:not(.hide)').forEach((visible_row, i) => {
        visible_row.style.backgroundColor = (i % 2 == 0) ? 'transparent' : ''
    }) 
}

const search5 = document.querySelector('.input-group5 input');
const table_rows5 = document.querySelectorAll('.table:nth-child(5) tbody tr');

search5.addEventListener('input',searchTable5);

function searchTable5(){
    table_rows5.forEach((row,i) => {
        let table_data = row.textContent.toLowerCase(),
            search_data = search5.value.toLowerCase();

        row.classList.toggle('hide',table_data.indexOf(search_data) < 0);
        row.style.setProperty('--delay', i / 25 + 's')
    })

    document.querySelectorAll('.table:nth-child(5) tbody tr:not(.hide)').forEach((visible_row, i) => {
        visible_row.style.backgroundColor = (i % 2 == 0) ? 'transparent' : ''
    }) 
}