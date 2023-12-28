print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name = name1.upper() + name2.upper()
msg = None
T = name.count('T')
R = name.count('R')
U = name.count('U')
E = name.count('E')
L = name.count('L')
O = name.count('O')
V = name.count('V')
E = name.count('E')

true_love = int(str(T+R+U+E) + str(L+O+V+E))

if not(10 < true_love <= 90):
    msg = f'Your score is {true_love}, you go together like coke and mentos.'
elif 40 <= true_love <= 50:
    msg = f'Your score is {true_love}, you are alright together.'
else:
    msg = f'Your score is {true_love}'

print(msg)
