// make three dicts variables for every choiche which can be made
// make input for the player choice
// make random choice for the computer
// make function which determinates who is winning the round
// make variable for the wins/looses of each player (while loop maybe)
// print who wins and loses each round and the final winner

function game(playerChoice, computerChoice) {
    playerRoudnWin = false
    if (playerChoice === computerChoice) {
        return `This round is a tie! You both chose ${computerChoice.toUpperCase()}`
    }
    if (playerChoice == 'rock') {
        if (rock[computerChoice]) {
            playerWon++;
            playerRoudnWin = true;

        };

    } else if (playerChoice == 'scissors') {
        if (scissors[computerChoice]) {
            playerWon++;
            playerRoudnWin = true;

        };
    } else {
        if (paper[computerChoice]) {
            playerWon++;
            playerRoudnWin = true;

        };
    };
    if (playerRoudnWin) {
        return `You won the round! ${playerChoice.toUpperCase()} beats ${computerChoice.toUpperCase()}!`;
    }
    computerWon++;
    playerRoudnWin = false;
    return `You lost the round! ${computerChoice.toUpperCase()} beats ${playerChoice.toUpperCase()}!`;
}

function playGame() {
    
    let randomChoiceComputer = computerChoices[Math.floor(Math.random() * computerChoices.length)];
    
    let currentText = game(playerChoice, randomChoiceComputer)
    let resultDiv = document.querySelector('.result-area')
    let scoreTextHuman = `HUMAN: ${playerWon}`
    let scoreTextComputer = `COMPUTER: ${computerWon}`
    let scoreDivHuman = document.querySelector('.human')
    let scoreDivComputer = document.querySelector('.computer')
    scoreDivComputer.textContent = scoreTextComputer
    scoreDivHuman.textContent = scoreTextHuman


    resultDiv.textContent = currentText
    

    if (playerWon == 5 || computerWon == 5){
        resultDiv.textContent = playerWon > computerWon ?
        `YOU WIN BY ${playerWon - computerWon} POINTS!` :
        `YOU LOST BY ${computerWon - playerWon} POINTS!`
        computerWon = 0
        playerWon = 0
    }
    
    // ensure that you can't enter empty string
    // if (playerChoice == '') {
    //     alert('Please insert ROCK, PAPER OR SCISSORS next time!!!')
    //     continue
    // }
    // playerChoice = playerChoice.toLowerCase()

    // // ensures that you can't enter anything different than rock, paper or scissors
    // if (playerChoice != 'rock' && playerChoice != 'paper' && playerChoice != 'scissors') {
    //     alert('Please enter valid value! ROCK, PAPER, OR SCISSORS')
    //     continue
    // }

    
    // if (playerRoudnWin) {
    //     console.log(`You won the round! ${playerChoice.toUpperCase()} beats ${randomChoiceComputer.toUpperCase()}!`);
    // }else{
    //     console.log(`You lost the round! ${randomChoiceComputer.toUpperCase()} beats ${playerChoice.toUpperCase()}!`)
    // }
    // gameCount++;

}


// if (playerWon > computerWon) {
//     console.log(`YOU WIN BY ${playerWon - computerWon} POINTS!`)
// } else if (computerWon > playerWon) {
//     console.log(`YOU LOST BY ${computerWon - playerWon} POINTS!`)
// } else {
//     console.log('IT\'s a TIE I GUESS')
// }

let rock = { scissors: true, paper: false };
let scissors = { paper: true, rock: false };
let paper = { rock: true, scissors: false };
let computerChoices = ['rock', 'paper', 'scissors'];

let gameCount = 0;
let playerWon = 0;
let computerWon = 0;
let playerRoudnWin = false

let playerChoice;

const buttons = document.querySelectorAll('.btn');


buttons.forEach(button => button.addEventListener('click', () => {
    let text = button.textContent
    playerChoice = text.toLowerCase()
    playGame()
}))



