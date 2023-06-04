from word_list import list_of_words
from random import choice as chs
from string import ascii_uppercase as aupper
alphabet = set(aupper)
valid_guesses = set()
word = chs(list_of_words)
word_letters = set(word)


def hangman():
    lives = 6
    current_word = ' '.join(el if el in valid_guesses else '_' for el in word) 
    print(f'Todays word is... {current_word}')
    while word_letters and lives > 0:
        guessed_letter = input('Guess a letter: ')
        
        if guessed_letter.upper() not in alphabet:
            print(f'------\nYou\'ve already guessed this letter, please try another one!')
            continue
        alphabet.remove(guessed_letter.upper())    
        if guessed_letter in word_letters:
            word_letters.remove(guessed_letter)
            valid_guesses.add(guessed_letter)
        else:
            print(f'------\nThere is no "{guessed_letter}" in the word!')
            lives -= 1
        word_condition = ' '.join(el if el in valid_guesses else '_' for el in word) 
        valid = '-> '.join(valid_guesses)
        print(f'------\nThis is the current state of the word: {word_condition}\nYou have {lives} lives remaining\nThis are the right letters you have guessed ({valid if valid else None})')
    if lives != 0:
        return f"Congrats the word is --{word.upper()}--"
    return f'The word was --{word.upper()}--. More luck next time!'
    
    

if __name__ == '__main__':
    print(hangman())

