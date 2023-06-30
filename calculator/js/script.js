// TODO LOOK AT WHAT BRANCH ARE YOU WORKING
// make numbers dissapear after clicking the sign 
// OR after clicking sing and starting to write
// make (%, +/- and .) work
function evaluate(arr) {
    
    while (arr[arr.length - 1] == '*' ||
        arr[arr.length - 1] == '-' ||
        arr[arr.length - 1] == '+' ||
        arr[arr.length - 1] == '/' ||
        arr[arr.length - 1] == '') {
        arr.pop()
    }
    console.log(arr)
    for (let i = 0; i < arr.length - 2; i += 2) {
        let currSum = 0
        let num1 = parseInt(arr[i])
        let num2 = parseInt(arr[i+ 2])
        if (arr[i + 1] == '+') {
            currSum = num1 + num2
            arr[i + 2] = currSum

        } else if (arr[i + 1] == '*') {
            currSum = arr[i] * arr[i + 2]
            arr[i + 2] = currSum
        } else if (arr[i + 1] == '-') {
            currSum = arr[i] - arr[i + 2]
            arr[i + 2] = currSum
        } else if (arr[i + 1] == '/') {
            currSum = arr[i] / arr[i + 2]
            arr[i + 2] = currSum
        } 
        sum = currSum
    }
    string = ''
    
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
let firstLen = 1
let sum = 0
let string = ''

clearBtn.addEventListener('click', () => {
    display.innerHTML = '0'
    sum = 0
})

allNumbers.forEach(number => number.addEventListener('click', () => {
    if(display.textContent == 0){
        display.innerHTML = ''
    }
    if (display.textContent.length <= 11) {
        display.textContent += number.value
    }
    
}))

add.addEventListener('click', () => {
    string += display.textContent
    string += ' + '
    
    display.innerHTML = ''
    if(string.split(' ').length > 4) {
        display.textContent = `${evaluate(string.split(' '))}`
        
    }
    
    
})


subtract.addEventListener('click', () => {
    string += display.textContent
    string += ' - '
    display.innerHTML = ''
    if(string.split(' ').length > 3) {
        display.textContent = `${evaluate(string.split(' '))}`
    }
})

multiply.addEventListener('click', () => {
    string += display.textContent
    string += ' * '
    display.innerHTML = ''
    if(string.split(' ').length > 3) {
        display.textContent = `${evaluate(string.split(' '))}`
    }
})

division.addEventListener('click', () => {
    string += display.textContent
    string += ' / '
    display.innerHTML = ''
    if(string.split(' ').length > 3) {
        display.textContent = `${evaluate(string.split(' '))}`
    }
})

equal.addEventListener('click', () => {
    string += display.textContent
    console.log(string)
    if(string.split(' ').length === 3) {
        display.textContent = `${evaluate(string.split(' '))}`
    }
    string = ''
})

