from Blackjack.strategies.basic import Basic_Strategy

class Player:
    def __init__(self, bankroll, betting_unit, strategy=Basic_Strategy()):
        self.hand = None
        self.bankroll = bankroll
        self.betting_unit = betting_unit
        self.strategy = strategy

    def bet(self):
        return self.betting_unit

    def play_turn(self, dealer_up_card):
         # Check if the player's hand is soft (contains an Ace counted as 11)
        is_soft = self.hand.is_soft()
        
        # Get dealer up card value
        dealer_card_value = dealer_up_card.get_value()

         # If hand is soft, use the soft totals strategy
        if is_soft:
            total_value = self.hand.calculate_value() - 11  # Subtracting 11 to convert Ace's value to 1
            action = self.strategy.SOFT_TOTALS_LOOKUP[total_value][dealer_card_value]
        # If hand is a pair, check for splitting strategy
        elif self.hand.is_pair():
            pair_value = self.hand.cards[0].get_value()
            action = 'split' if self.strategy.SPLIT_LOOKUP[pair_value][dealer_card_value] else 'hit'
        # If hand is hard, use the hard totals strategy
        else:
            total_value = self.hand.calculate_value()
            action = self.strategy.HARD_TOTALS_LOOKUP[total_value][dealer_card_value]
        
        # Optionally handle surrendering
        if total_value in self.strategy.SURRENDER_LOOKUP and self.strategy.SURRENDER_LOOKUP[total_value][dealer_card_value]:
            action = 'surrender'
        
        return action

    def win(self, amount):
        self.bankroll += amount

    def lose(self, amount):
        self.bankroll -= amount

