from Blackjack.deck import Deck

deck = Deck()
deck.shuffle()

for i in range(10):
    card = deck.deal()
    print(f"You got: {card}")
