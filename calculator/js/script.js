const allNumbers = document.querySelectorAll('.number')
const display = document.querySelector('.display p')
const clearBtn = document.querySelector('.clear')

const sumButton = document.querySelector

let sum = 0

clearBtn.addEventListener('click', () => {
    display.innerHTML = '0'
})

allNumbers.forEach(number => number.addEventListener('click', () =>{
    if(display.textContent == 0){
        display.innerHTML = ''
    }
    if(display.textContent.length <= 11) {
        display.textContent += number.value
    }
}))

