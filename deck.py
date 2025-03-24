import random

colors = ["Red", "Blue", "Green", "Yellow"]
numbers = list(range(10))

def create_deck():
    deck = [(color, 0) for color in colors]
    for color in colors:
        for number in range(1, 10):
            deck.append((color, number))
            deck.append((color, number))

    random.shuffle(deck)
    return deck
