import random



def main():
    print('Welcome to the Number Guessing Game!')
    print('I\'m thingking of a number between 1 and 100.')
    level = input('Choose a difficulty. Type \'easy\' or \'hard\': ')

    lives = 5 if level.lower() == 'hard' else 10
    rand_number = random.randint(1, 100)
    game_over = False

    while not game_over:
        print(f'You have {lives} attempts reamining to guess the number.')
        guess = int(input('Make a guess: '))

        if guess == rand_number:
            print('Win!')
            game_over = True
        
        if guess > rand_number:
            print('Too high.')
            lives -= 1

        if guess < rand_number:
            print('Too low.')
            lives -= 1

        if lives == 0:
            print('Lose!')
            game_over = True


if __name__ == "__main__" :
    main()