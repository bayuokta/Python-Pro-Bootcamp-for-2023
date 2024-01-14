from rich.console import Console
console = Console()
console.print('Welcome to the secret auction program.')
data_bid = {}
win = ""

while True:
    name = console.input('What is your name ?: ').lower()
    bid = int(console.input('What\'s your bid?: '))
    data_bid[name] = bid
    choice = console.input('Are there any other bidders? Type \'yes\' or \'no\' ').lower()
    if choice == 'no':
        break

win = max(data_bid, key=data_bid.get)
console.print(f'The winner is [green]{win}[/green] with a bid of ${data_bid.get(win)}')
    
