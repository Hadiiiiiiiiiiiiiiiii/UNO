def play(player_hand, ground_card, deck):
    print("\nYour hand:")
    for i, card in enumerate(player_hand):
        print(f"""
+-------+
|  {card[0]}  |
|   {card[1]}   |
|       |
+-------+
""")
    print(f"Card on the ground: {ground_card[0]} {ground_card[1]}")

    valid_moves = [i for i, card in enumerate(player_hand) if card[0] == ground_card[0] or card[1] == ground_card[1]]

    if not valid_moves:
        print("No valid moves! Drawing a card...")
        new_card = deck.pop(0) if deck else None
        if new_card:
            player_hand.append(new_card)
            print(f"You drew: {new_card[0]} {new_card[1]}")
        else:
            print("Deck is empty. No more draws.")
        return ground_card

    while True:
        try:
            choice = int(input(f"Select a card index from {valid_moves}: "))
            if choice in valid_moves:
                selected_card = player_hand.pop(choice)
                print(f"You played: {selected_card[0]} {selected_card[1]}")
                
                
                if len(player_hand) == 1:
                    call= input("Type UNO to call it: ").strip().lower()
                    if call == "uno":
                        print("UNO!")
                    else:
                        print("I just told you to call uno")
                        player_hand.append(deck.pop(0))
                        player_hand.append(deck.pop(0))
                        print("You drew two cards")
                return selected_card
            else:
                print("Invalid choice. Pick a valid card index.")
        except ValueError:
            print("Please enter a number.")
