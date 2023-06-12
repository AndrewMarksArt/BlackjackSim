class Card:
    """
    Represents a standard playing card with added functionality for the Red Seven Count card counting system.
    """

    def __init__(self, rank, suit):
        """
        Initialize the Card with a rank, suit, and calculate its value and count value for card counting.
        
        Args:
            rank (str): The rank of the card. One of ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'].
            suit (str): The suit of the card. One of ['hearts', 'diamonds', 'clubs', 'spades'].
        """
        self.rank = rank
        self.suit = suit
        self.is_ace = (rank == 'A')
        self.value = self._set_value()
        self.count_value = self._set_count_value()

    def _set_value(self):
        """
        Assigns a value to the card based on its rank for the game of Blackjack.
        
        Returns:
            int: The value of the card.
        """
        if self.rank.isdigit():
            return int(self.rank)
        elif self.rank == 'A':
            return 11
        else:
            return 10

    def _set_count_value(self):
        """
        Assigns a count value to the card based on its rank and suit for the Red Seven Count card counting system.
        
        Returns:
            int: The count value of the card.
        """
        if self.rank in ['2', '3', '4', '5', '6']:
            return 1
        elif self.rank == '7' and self.suit in ['hearts', 'diamonds']:
            return 1
        elif self.rank in ['10', 'J', 'Q', 'K', 'A']:
            return -1
        else:
            return 0
