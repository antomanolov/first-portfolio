// TODO LOOK AT WHAT BRANCH ARE YOU WORKING
// make (%, +/- and .) work

// function that takes the place of eval()
// it takes every second index [1, '+' , 2]
//  and executest the action with the operator
function evaluate(arr) {
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
    string = [sum,]
    return sum
}


// function that ensures operators will be used only once even if clicked more than that
function lastIndex(arr) {
    if (arr.slice(-1) != '+' &&
    arr.slice(-1) != '-' &&
    arr.slice(-1) != '/' &&
    arr.slice(-1) != '*') {
        return true
    }
    return false
}

// this function is made to ensure that every 2 numbers will be immediately reduced to one 
function action(operator) {
    if (display.textContent != ''){
        string.push(parseInt(display.textContent))
    }
    
    if (string.length >= 3) {
        
        num = evaluate(string)
        display.textContent = num
        string.push(operator)
    } 
    if (lastIndex(string)) {
        display.innerHTML = ''
        string.push(operator)
    }
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
let string = []

clearBtn.addEventListener('click', () => {
    display.innerHTML = '0'
    string = []
    sum = 0
})

allNumbers.forEach(number => number.addEventListener('click', () => {
    if(display.textContent == 0 || display.textContent == string[0]){
        display.innerHTML = ''
    }
    
    if (display.textContent.length <= 11) {
        display.textContent += number.value
    }
    
    
    
}))

add.addEventListener('click', () => {
    action('+')
})


subtract.addEventListener('click', () => {
   action('-')
})

multiply.addEventListener('click', () => {
    action('*')
})

division.addEventListener('click', () => {
    action('/')
})

equal.addEventListener('click', () => {
    if(display.textContent != ''){
        string.push(parseInt(display.textContent))
    }
    
    display.textContent = `${evaluate(string)}`
    
    string = []
})

