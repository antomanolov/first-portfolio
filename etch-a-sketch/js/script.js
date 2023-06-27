let allGridSquares = document.querySelectorAll('.square')
let btn = document.querySelector('.number-choose')
let gridNumber = document.querySelector('input')
let grid = document.querySelector('.square-container')

function putClassSquare() {
    const newDiv = document.createElement('div')
    newDiv.classList.add('square')
    return newDiv
}

function gridValue() {
    if (gridNumber.value === '' || gridNumber.value > 100) {
        gridNumber.value = 100;
    } else if (gridNumber.value < 9) {
        gridNumber.value = 9;
    }
    const value = +gridNumber.value
    
    return value
}

function gridCreate(numInput, color) {
    // adding correct properties to the grid
    grid.style.setProperty("grid-template-columns", `repeat(${numInput}, 2fr)`);
    grid.style.setProperty("grid-template-rows", `repeat(${numInput}, 2fr)`);
    for (let i = 0; i < numInput * numInput; i++) {
        // putting the class square on every div
        grid.append(putClassSquare())
    }
    allGridSquares = document.querySelectorAll('.square')
    allGridSquares.forEach(square => square.addEventListener(
        'mouseover', () => {
            square.style.backgroundColor = color
        }
    ));
}


btn.addEventListener('click', () => {
    // on every button click we delete all divs and make space for new ones
    grid.innerHTML = ''

    // evaluate grid value properly
    const userInput = gridValue()
    gridCreate(userInput, 'black')


})

let circleColor = document.querySelectorAll('.color')
circleColor.forEach(cirle => {
    cirle.addEventListener('click', ()=>{
        
    })
})
