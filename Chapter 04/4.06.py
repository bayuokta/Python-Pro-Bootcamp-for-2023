rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
# 0 rock, 1 paper, 2 scissor
hand = [rock, paper, scissors]
result = ['Win', 'Lose', 'Draw']
result = None

bot = random.randint(0, 2)
user = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n'))

# print(f'Bot = {bot}, User = {user}')

print(hand[user])

print('Computer chose:')

print(hand[bot])

if bot == 0 and user == 1:
    print('You win.')
elif bot == 0 and user == 2:
    print('You Lose.')
elif bot == 1 and user == 0:
    print('You Lose.')
elif bot == 1 and user == 2:
    print('You Win.')
elif bot == 2 and user == 0:
    print('You Win.')
elif bot == 2 and user == 1:
    print('You Lose.')
else:
    print('Draw.')
