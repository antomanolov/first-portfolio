function evaluate (arr) {
    
    let equality = arr.split(' ')
    if(equality[1] == '+'){
        sum = parseInt(equality[0]) + parseInt(equality[2])
    }else if(equality[1] == '-'){
        sum = parseInt(equality[0]) - parseInt(equality[2])
    }else if(equality[1] == '*'){
        sum = parseInt(equality[0]) * parseInt(equality[2])
    }else{
        sum = parseInt(equality[0]) / parseInt(equality[2])
    }
    return sum
}

const allNumbers = document.querySelectorAll('.number')
const display = document.querySelector('.display p')
const clearBtn = document.querySelector('.clear')

const division = document.querySelector('.division')
const multiply = document.querySelector('.multiply')
const add = document.querySelector('.add')
const subtract = document.querySelector('.subtract')
const equal = document.querySelector('.equal')


// const sumButton = document.querySelector

let sum = 0

clearBtn.addEventListener('click', () => {
    display.innerHTML = '0'
    sum = 0
})

allNumbers.forEach(number => number.addEventListener('click', () =>{
    if(display.textContent == 0){
        display.innerHTML = ''
    }
    if(display.textContent.length <= 11) {
        display.textContent += number.value
    }
}))

add.addEventListener('click', () =>{
    sum += display.textContent
    sum +=' + '
    console.log(sum)
   
    display.textContent = evaluate(sum)
    
    display.innerHTML = ''
    
})


subtract.addEventListener('click', () =>{
    sum = display.textContent
    sum +=' - '
    display.innerHTML = ''
    evaluate(sum)
})

multiply.addEventListener('click', () =>{
    sum = display.textContent
    sum +=' * '
    display.innerHTML = ''
    evaluate(sum)
})

division.addEventListener('click', () =>{
    sum = display.textContent
    sum +=' / '
    display.innerHTML = ''
    evaluate(sum)
})

equal.addEventListener('click', () =>{
    sum += display.textContent
    display.textContent = evaluate(sum)
})

