from random import randint as rdin

def guess(low_end, high_end):
    random_number = rdin(low_end , high_end)
    while True:
        try:
            guess = int(input(f'Now you must guess the number, what is your choice of number?: '))
        except ValueError:
            print('Please next time type a number!')
            continue
        if guess > random_number:
            print('----Your choice is too high!')
        elif guess < random_number:
            print('--- Your choice is too low!')
        else:
            print(f'Congrats you\'ve guessed right the number is {random_number}! *throwing some confetti*')
            break
        
while True:
    try:
        low = int(input(f'Choose lowest possible number: '))
        high = int(input(f'Choose highest possible number: '))
        break
    except ValueError:
        print('Enter valid numbers next time!')
guess(low, high)