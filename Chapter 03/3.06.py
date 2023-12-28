# Multiple if statement
print('Welcome to the rollercoaster!')
height = int(input('Whats is your height in cm? '))

if height > 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is your age? '))
    bill = None
    if age < 12:
        bill = 5
        print('Please pay $5')
    elif age <= 18:
        bill = 7
        print('Please pay $7')
    else:
        bill = 12
        print('Please pay $12') 

    wants_photo = input('Do you want a photo take? Y or N. ')
    if wants_photo == 'Y':
        bill += 3
    
    print(f'Your final bill is {bill}')
else:
    print('Sorry, yuo have to grow taller before you can ride.')