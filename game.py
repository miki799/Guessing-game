import sys
from random import randint

# guessing game started through terminal
try:
    start = int(sys.argv[1])
    stop = int(sys.argv[2])
    print(
        "### Guessing game ###\n"
        f"Range of numbers you need to guess from is: ({start}, {stop})\n\n"
    )
    y = randint(start, stop)  # draws a number
    # print(f'correct answer: {y}')
except (IndexError, ValueError):  # IndexError if no parameters provided, and ValueError if they are not numbers
    print(
        'You need to provide integer parameters.'
        'They will specify the range of numbers '
        'from which you will have to guess'
    )
    exit()

while True:
    try:
        x = int(input('Guess a number...\t'))
        if start <= x <= stop:
            if x == y:
                print('Congratulations!!! You have guessed the number')
                break
            else:
                print('Bad luck... Keep trying')
        else:
            print(f'You need to guess a number between ({start}, {stop})')
    except ValueError:
        print('You need to enter a integer...')
        continue
