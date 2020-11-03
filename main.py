from random import randint
# only used for testing
import sys


def guess_game(input, answer):
    try:
        if 0 < input < 11:
            if input == answer:
                print('you are a genius!')
                return True
            else:
                return False
        else:
            print('hey bozo, I said 1~10')
            return False
    except TypeError:
        return False


if __name__ == '__main__':
    answer = randint(int(sys.argv[1]), int(sys.argv[2]))
    while True:
        try:
            guess = int(input(f'guess a number {sys.argv[1]} ~ {sys.argv[2]}:  '))
            if guess_game(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue

