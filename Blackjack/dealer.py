from Blackjack.player import Player

class Dealer(Player):
    """
    This class represents a Blackjack dealer, extending the Player class.
    
    The dealer has a specific set of rules it must follow, which are 
    encapsulated within this class.
    """
    def __init__(self):
        """
        Initializes a Dealer object. Dealers do not have a name or a bankroll, 
        so these are not required during the initialization of a Dealer.
        """
        super().__init__(None, None)

    def decide_next_move(self, hand, dealer_card=None):
        """
        Decides the dealer's next move given a hand and a dealer card. 

        According to standard Blackjack rules, the dealer must hit if the value 
        of their hand is less than 17, and stand otherwise.

        Args:
            hand (Hand): The dealer's current hand.
            dealer_card (Card, optional): The dealer's face-up card. This 
            argument is not used in the dealer's decision in standard Blackjack 
            rules and is thus optional.

        Returns:
            str: 'H' if the dealer should hit, 'S' if the dealer should stand.
        """
        return 'H' if hand.value < 17 else 'S'
