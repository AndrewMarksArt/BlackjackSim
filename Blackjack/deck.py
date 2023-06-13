import random
from Blackjack.card import Card  

class Deck:
    """
    This class represents a deck of cards.
    """
    def __init__(self):
        self.suits = ['hearts', 'diamonds', 'clubs', 'spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = self.create_deck()

    def create_deck(self):
        """
        This method creates a deck of cards by iterating through all suits and ranks.
        Each combination of suit and rank is used to create a Card object.
        """
        return [Card(suit, rank) for suit in self.suits for rank in self.ranks]

