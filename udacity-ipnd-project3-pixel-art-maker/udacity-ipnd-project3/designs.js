//Defining some variables
const table = document.getElementById("pixelCanvas");
const colorPicker = document.getElementById("colorPicker");
const sizePicker = document.getElementById('sizePicker');
const cells = document.getElementsByTagName('td');


//Creating a grid with row and column that will create cells
function makeGrid() {

    let height = document.getElementById('inputHeight').value;
    let width = document.getElementById('inputWidth').value;

    // Your code goes here!
    //grid is empty, cells will added by user input value in tables inner html

    table.innerHTML = '';
    var tbody = document.createElement('tbody');
    // create table row which will be row and for each row creates table data which will be like column for grid
    for (var i = 0; i < height; i++) {
        var tr = document.createElement('tr');
        for (var j = 0; j < width; j++) {
            var td = document.createElement('td');
            td.appendChild(document.createTextNode(''));
            tr.appendChild(td);
        }
        tbody.appendChild(tr);
    }
    table.appendChild(tbody);

    //Goes over all the cells which are td elements, add event listener to color selected cell 
    for (let i = 0; i < cells.length; i++) {
        cells[i].addEventListener("click", function (event) {
            event.target.style.backgroundColor = document.getElementById('colorPicker').value;
        });
    }
}

// When size picker is submitted by the user, run makeGrid 
//After pressing submit query button

sizePicker.addEventListener('submit', function(event) {
  event.preventDefault();
  // When the data is submitted the grid mount function is called
  makeGrid();
});


// Default grid as a sample.
makeGrid();