from collections import Counter
def computer_play(comphand, ground_card, deck):
    print("\nComputer's turn...")
    print(f"Computer has {len(comphand)} cards.")

    counts=Counter([card[0] for card in comphand])
    bestcolor = max(counts, key=counts.get)
    valid_moves = [card for card in comphand if card[0] == ground_card[0] or card[1] == ground_card[1] and card[0]==bestcolor]

    if not valid_moves:
        print("Computer has no valid moves! Drawing a card...")
        new_card = deck.pop(0) if deck else None
        if new_card:
            comphand.append(new_card)
            print(f"Computer drew a card.")
        else:
            print("Deck is empty. Computer cannot draw.")
        return ground_card

    selected_card = valid_moves[0]
    comphand.remove(selected_card)
    print(f"Computer played: {selected_card[0]} {selected_card[1]}")

    return selected_card
