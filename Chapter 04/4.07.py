import random
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

# Write your code below this line 👇

# 0 rock, 1 paper, 2 scissor
hand = [rock, paper, scissors]
result = {
    (0, 1): 'You win.', 
    (0, 2): 'You Lose.',
    (1, 0): 'You Lose.', 
    (1, 2): 'You Win.',
    (2, 0): 'You Win.', 
    (2, 1): 'You Lose.',
    (0, 0): 'Draw.', 
    (1, 1): 'Draw.', 
    (2, 2): 'Draw.'
}

bot = random.randint(0, 2)
user = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n'))

print(hand[user])

print('Computer chose:')

print(hand[bot])

print(result.get((bot,user), 'Invalid input'))