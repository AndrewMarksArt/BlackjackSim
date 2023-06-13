from Blackjack.hand import Hand

class Player:
    """
    A class representing a blackjack player.

    Attributes
    ----------
    bankroll : int
        The amount of money the player has to bet with.
    min_bet : int
        The minimum amount the player can bet.
    hands : list
        A list of Hand objects representing the hands the player is currently playing.
    """

    def __init__(self, bankroll, min_bet):
        """
        Constructs all the necessary attributes for the player object.

        Parameters
        ----------
            bankroll : int
                The amount of money the player has to bet with.
            min_bet : int
                The minimum amount the player can bet.
        """
        self.bankroll = bankroll
        self.min_bet = min_bet
        self.hands = []

    def deal_hand(self, card1, card2):
        """
        Deals a new hand to the player.

        Parameters
        ----------
            card1 : Card
                The first card of the hand.
            card2 : Card
                The second card of the hand.
        """
        self.hands.append(Hand(card1, card2))

    def place_bet(self):
        """
        Places a bet by the player. The bet is deducted from the player's bankroll.

        Returns
        -------
        int
            The amount of the bet.
        """
        self.bankroll -= self.min_bet
        return self.min_bet

    def receive_winnings(self, amount):
        """
        Adds the winning amount to the player's bankroll.

        Parameters
        ----------
            amount : int
                The amount of the winnings.
        """
        self.bankroll += amount

    def can_split(self, hand):
        """
        Checks if a given hand can be split.

        Parameters
        ----------
            hand : Hand
                The hand to check.

        Returns
        -------
        bool
            True if the hand can be split, False otherwise.
        """
        return len(hand.cards) == 2 and hand.cards[0].rank == hand.cards[1].rank

    def decide_next_move(self, hand, dealer_card):
        """
        Decides the player's next move. To be implemented in subclasses, according to the player's strategy.

        Parameters
        ----------
            hand : Hand
                The current hand the player is playing.
            dealer_card : Card
                The dealer's face-up card.

        Raises
        ------
        NotImplementedError
            If the method is not implemented in a subclass.
        """
        raise NotImplementedError

    def reset(self):
        """
        Resets the player's hands, to be ready for a new round.
        """
        self.hands = []
