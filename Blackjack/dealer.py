class Dealer:
    def __init__(self):
        self.hand = None

    def offer_insurance(self):
        pass

    def play_turn(self):
        while self.hand.calculate_value() < 17:
            return 'hit'
        return 'stand'

