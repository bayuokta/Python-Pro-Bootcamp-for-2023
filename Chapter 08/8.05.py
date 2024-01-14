alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    msg = ''
    if direction == 'decode':
            shift *= -1 
    for i in text:
        position = alphabet.index(i)
        new_position = position + shift
        msg += alphabet[new_position]
    print(f'The {direction} text is {msg}')

    # if direction == 'encode':
    #     for i in text:
    #         index = alphabet.index(i) + shift
    #         msg += alphabet[index]
    # elif direction == 'decode':
    #     for i in text:
    #         index = alphabet.index(i) - shift
    #         msg += alphabet[index]
    

caesar(text, shift, direction)

