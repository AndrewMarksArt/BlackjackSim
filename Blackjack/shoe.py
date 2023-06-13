import random
from Blackjack.card import Card
from Blackjack.deck import Deck

class Shoe:
    """
    This class represents a shoe in blackjack, which is a device that holds multiple decks of cards.
    """
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.cards = self.create_shoe()

    def create_shoe(self):
        """
        This method creates a shoe by repeating the cards in a deck a number of times equal to num_decks.
        """
        return [card for _ in range(self.num_decks) for card in Deck().cards]

    def shuffle(self):
        """
        This method shuffles the cards in the shoe.
        """
        random.shuffle(self.cards)

    def deal_card(self):
        """
        This method deals a card from the shoe.
        """
        return self.cards.pop()

    def needs_shuffle(self, penetration=0.75):
        """
        This method determines if the shoe needs to be shuffled.
        It returns True if 75% of the cards have been dealt, and False otherwise.
        """
        return len(self.cards) < self.num_decks * 52 * (1 - penetration)
