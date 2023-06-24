from random import randint

# get a deck of 52 cards
signs = ['Hearts', 'Diamonds', 'Spade', 'Club']
numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10']
deck = []

for i in numbers:
    for j in signs:
        deck.append(f'{i}, {j}')

# Fisher and Yates shuffle
for i in range(len(deck) - 1):
    j = randint(0, i)
    deck[i], deck[j] = deck[j], deck[i]

print(deck)
