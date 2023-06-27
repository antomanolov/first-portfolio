let allGridSquares = document.querySelectorAll('.square')
let btn = document.querySelector('.number-choose')
let gridNumber = document.querySelector('input')
let grid = document.querySelector('.square-container')

function putClassSquare () {
    const newDiv = document.createElement('div')
    newDiv.classList.add('square')
    return newDiv
}



btn.addEventListener('click', () => {
    grid.innerHTML = ''
    if(gridNumber.value === '' || gridNumber.value > 100){
        gridNumber.value = 100;
    }else if(gridNumber.value < 9){
        gridNumber.value = 9;
    }
    grid.style.setProperty("grid-template-columns", `repeat(${gridNumber.value}, 2fr)`);
    grid.style.setProperty("grid-template-rows", `repeat(${gridNumber.value}, 2fr)`);
    
    for (let i = 0; i < gridNumber.value * gridNumber.value; i++){
            grid.append(putClassSquare())
    }
    allGridSquares = document.querySelectorAll('.square')
    allGridSquares.forEach(square => square.addEventListener(
        'mouseover', () => {
            if (square.style.backgroundColor === 'black'){
            square.style.backgroundColor = 'white'
            }else{
                square.style.backgroundColor = 'black'
            };
        } 
    ));
    
    console.log(allGridSquares)
    
})


