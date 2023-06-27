let allGridSquares = document.querySelectorAll('.square')
let btn = document.querySelector('.refresh')
let gridNumber = document.querySelector('input')
let grid = document.querySelector('.square-container')
let circleColor = document.querySelectorAll('.color')

function gridCreate(numInput) {
    // adding correct properties to the grid
    grid.style.setProperty("grid-template-columns", `repeat(${numInput}, 2fr)`);
    grid.style.setProperty("grid-template-rows", `repeat(${numInput}, 2fr)`);
    for (let i = 0; i < numInput * numInput; i++) {
        // putting the class square on every div
        grid.append(putClassSquare())
    }
    
};


function putClassSquare() {
    const newDiv = document.createElement('div');
    newDiv.classList.add('square');
    return newDiv;
};

function circleColoring (color) {
    allGridSquares = document.querySelectorAll('.square')
    allGridSquares.forEach(square => square.addEventListener(
        'mouseover', () => {
            square.style.backgroundColor = color
        }
    ));
};

// getting the right min and max grid value without fail
function gridValue() {
    if (gridNumber.value === '' || gridNumber.value > 100) {
        gridNumber.value = 100;
    } else if (gridNumber.value < 9) {
        gridNumber.value = 9;
    };
    const value = +gridNumber.value;
    
    return value;
};



// trying the 'change' event, maybe click is better cuz when refreshed you 
// can't output the same grid again before putting new value

gridNumber.addEventListener('change', () => {
    // on every button click we delete all divs and make space for new ones
    grid.innerHTML = ''

    // evaluate grid value properly
    const userInput = gridValue()
    gridCreate(userInput, 'black')


})

// adding the right color value to mouseover
circleColor.forEach(cirle => {
    cirle.addEventListener('click', ()=>{
        circleColoring(cirle.classList[0]);
    })
})

// refresh button
btn.addEventListener('click', () =>{
    grid.innerHTML = ''
})