from deck import create_deck
from player import play
from computer import computer_play

def start_game(deck):
    player_hand = deck[:5]
    comphand = deck[:5]
    ground_card = deck.pop(0)
    return player_hand, comphand, ground_card

def main():
    deck = create_deck()
    player_hand, comphand, ground_card = start_game(deck)

    while True:
        ground_card = play(player_hand, ground_card, deck)
        if not player_hand:
            return"Congratulations! You won! 🎉"
            

        ground_card = computer_play(comphand, ground_card, deck)
        if not comphand:
            return"Computer wins! Better luck next time. 🤖"
            

if __name__ == "__main__":
    main()