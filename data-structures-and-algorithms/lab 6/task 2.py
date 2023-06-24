alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
encrypted_word = []

word = input('Enter word to encrypt: ')
shift_val = int(input('Enter jump of value for encryption: '))

for i in word:
    for letter_index, letter_val in enumerate(alphabets):
        if i == letter_val:
            if (letter_index + shift_val) >= 25:
                encrypted_word.append(alphabets[shift_val - (26 - letter_index)])
            else:
                encrypted_word.append(alphabets[letter_index + shift_val])
        elif i == ' ':
            encrypted_word.append(' ')
            break

print(''.join(encrypted_word))
