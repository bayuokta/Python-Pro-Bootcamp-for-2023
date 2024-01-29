import random 

user_cards = []
computer_cards = []
is_game_over = False

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    if user_score > 21:
        print(f'Your cards: {user_cards}')
        print(f'Computer\'s first card: {computer_cards[0]}')

        break
    
    print(f'Your cards: {user_cards}')
    print(f'Computer\'s first card: {computer_cards[0]}')
    next = input('Type \'y\' to get another card, type \'n\' to pass:')

    while sum(computer_cards) <= 16:
        computer_cards.append(deal_card())

    print(user_score, computer_score)
    
    if next == 'y':
        user_cards.append(deal_card())
        
    else:
        is_game_over = True

    