from Blackjack.deck import Deck
from Blackjack.hand import Hand

deck = Deck()
deck.shuffle()

for i in range(10):

    hand = Hand()
    print(f"Hand: {i+1}")

    hand.add_card(deck.deal())
    hand.add_card(deck.deal())
    print(f"Your hand: {hand.cards[0]}, {hand.cards[1]}")
    print(f"Hand value: {hand.calculate_value()}")
    

    while hand.calculate_value() < 17:
        hand.add_card(deck.deal())
        print(f"Dealt: {hand.cards[-1]}")
        print(f"Hand: ")
        for i in range(len(hand.cards)):
            print(hand.cards[i])
        print(f"Hand value: {hand.calculate_value()}")

    print()
