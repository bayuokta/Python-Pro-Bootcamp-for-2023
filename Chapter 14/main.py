import random
from data import data
import os
from art import logo, vs


def main():
    score = 0
    a = random.choice(data)
    b = random.choice(data)
    while True:
        a = b
        b = random.choice(data)

        if a == b:
            b = random.choice(data)

        print(logo)
        if score > 0:
            print(f'You\'re right! Current score: {score}.')
        print(f'Compare A: {a.get('name')}, a {a.get('description')}, from {
              a.get('country')}')
        print(vs)
        print(f'Against B: {b.get('name')}, a {b.get('description')}, from {
              b.get('country')}')
        answer = input('Who has more followers? Type \'A\' or \'B\': ')

        if answer.lower() == 'a':
            if a.get('follower_count') > b.get('follower_count'):
                score += 1
            else:
                os.system('cls')
                break
        elif answer.lower() == 'b':
            if b.get('follower_count') > a.get('follower_count'):
                score += 1
            else:
                os.system('cls')
                break
        else:
            os.system('cls')
            break

        os.system('cls')
    print(logo)
    print(f'Sorry, that\'s wrong. Final score: {score}')


if __name__ == '__main__':
    main()
