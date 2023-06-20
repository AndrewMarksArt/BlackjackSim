class Player:
    def __init__(self, bankroll, betting_unit, strategy):
        self.hand = None
        self.bankroll = bankroll
        self.betting_unit = betting_unit
        self.strategy = strategy

    def bet(self):
        return self.betting_unit

    def play_turn(self, dealer_up_card):
        return 'stand'

    def win(self, amount):
        self.bankroll += amount

    def lose(self, amount):
        self.bankroll -= amount

