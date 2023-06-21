from Blackjack.strategies.basic import Basic_Strategy

class Player:
    def __init__(self, bankroll, betting_unit, strategy=None):
        self.hand = None
        self.bankroll = bankroll
        self.betting_unit = betting_unit
        # Initialize strategy
        if strategy is None:
            self.strategy = Basic_Strategy()
        else:
            self.strategy = strategy

    def bet(self):
        return self.betting_unit

    def play_turn(self, dealer_up_card):
        # Check if Dealer up card is an Ace
        if dealer_up_card.value == 'A':
            print("Dealer offers players insurance.")
            if Basic_Strategy.TAKE_INSURANCE:
                print("player takes insurance.")
            else:
                print("player refused insurance.")
        else:
            print("Dealer doesn't have an Ace showing.")

        # Check if the player has a Blackjack
        if len(self.hand.cards) == 2 and self.hand.calculate_value() == 21:
            print("Player has Blackjack!")
            return 'blackjack'
        else:
            print("Player doesn't have Blackjack.")

        


    def win(self, amount):
        self.bankroll += amount

    def lose(self, amount):
        self.bankroll -= amount
