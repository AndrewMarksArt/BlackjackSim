class Hand:
    """
    The Hand class represents a hand of cards in a blackjack game.
    """
    def __init__(self, card1, card2):
        """
        Initialize a hand with two cards.
        
        Args:
        card1 (Card): The first card in the hand.
        card2 (Card): The second card in the hand.
        """
        self.cards = [card1, card2]
        self.value = self._calc_value()
        self.soft = self._check_soft()

    def _calc_value(self):
        """
        Calculate the total value of the hand.

        Returns:
        int: The total value of the hand.
        """
        return sum(card.value for card in self.cards)

    def _check_soft(self):
        """
        Check if the hand is soft (contains an ace).

        Returns:
        bool: True if the hand is soft, False otherwise.
        """
        return any(card.rank == 'A' for card in self.cards)

    def add_card(self, card):
        """
        Add a card to the hand and update the value and soft attributes.

        Args:
        card (Card): The card to add to the hand.
        """
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'A':
            self.soft = True
        self.adjust_for_ace()

    def adjust_for_ace(self):
        """
        Adjust the value of the hand for aces when the total value exceeds 21.
        
        If the hand is soft (contains an ace) and the total value is over 21,
        subtract 10 from the total value and change the hand to hard (no aces).
        """
        while self.value > 21 and self.soft:
            self.value -= 10
            self.soft = False

    def is_bust(self):
        """
        Check if the hand is a bust (total value over 21).

        Returns:
        bool: True if the hand is a bust, False otherwise.
        """
        return self.value > 21

    def is_blackjack(self):
        """
        Check if the hand is a blackjack (two cards totaling 21).

        Returns:
        bool: True if the hand is a blackjack, False otherwise.
        """
        return len(self.cards) == 2 and self.value == 21
