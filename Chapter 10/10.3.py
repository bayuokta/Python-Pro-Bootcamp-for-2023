logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(a, b):
    return a + b

def divide(a, b):
    return a - b

def pembagian(a, b):
    return a / b

def multiply(a, b):
    return a * b

operations = {
    '+': add,
    '-': divide,
    '*': multiply,
    '/': pembagian
}


symbols = '+\n-\n*\n/'
print(logo)
result = 0



def app():
    result = 0
    a = float(input('What\'s the first number?: '))
    print(symbols)
    symbol = input('Pick an operation: ')
    
    b = float(input('What\'s the next number?: '))
    result = operations.get(symbol)(a, b)
    print(f'{a} {symbol} {b} = {result}')
    choice = input(f'Type \'y\' to continue calculation with {result}, or type \'n\' to start a new calculation: ')
    if choice.lower() == 'n':
        app()
    elif choice.lower() == 'y':
        def app1(result):
            c = float(input('What\'s the next number?: '))
            print(symbols)
            symbol = input('Pick an operation: ')
            result = operations.get(symbol)(result, c)
            print(f'{result} {symbol} {c} = {result}')
            choice = input(f'Type \'y\' to continue calculation with {result}, or type \'n\' to start a new calculation: ')
            if choice.lower() == 'n':
                app()   
            elif choice.lower() == 'y':
                app1(result)
            else:
                return
        app1(result)
    else:
        return








app()


