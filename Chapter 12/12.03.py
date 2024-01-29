import random
import os

EASY_LEVEL_TURNS = 5
HARD_LEVEL_TURNS = 10


def set_difficulty(level: str):
    return EASY_LEVEL_TURNS if level.lower() == 'hard' else HARD_LEVEL_TURNS


def display():
    logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print('I\'m thingkin of a number between 1 and 100.')


def check_answer(guess: int, rand_number: int):
    if guess == rand_number:
        return True

    if guess > rand_number:
        print('Too high.')
        return False

    if guess < rand_number:
        print('Too low.')
        return False


def main():
    display()
    level = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    lives = set_difficulty(level)
    rand_number = random.randint(1, 100)
    game_over = False

    while lives != 0:
        print(f'You have {lives} attempts reamining to guess the number.')
        guess = int(input('Make a guess: '))
        # os.system('cls')
        # display()

        if check_answer(guess, rand_number):
            game_over = True
            break
        else:
            lives -= 1

    print('Win!' if game_over else 'Lose!')


if __name__ == "__main__":
    main()
