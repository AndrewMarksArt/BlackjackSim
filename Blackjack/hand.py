class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card.value.isnumeric():
                value += int(card.value)
            elif card.value in ['J', 'Q', 'K']:
                value += 10
            elif card.value == 'A':
                aces += 1
                value += 11

        # Adjust for aces (11 or 1)
        while aces > 0 and value > 21:
            value -= 10
            aces -= 1
        
        return value

    
    def is_soft(self):
         # Check if the hand is soft (contains an Ace counted as 11)
        return any(card.value == 'A' for card in self.cards) and self.calculate_value() <= 21

    def is_pair(self):
        # Check if the hand is a pair (two cards of the same value)
        return len(self.cards) == 2 and self.cards[0].value == self.cards[1].value

    def is_blackjack(self):
        # Check if the hand is a blackjack (Ace and any card with a value of 10)
        return any(card.value == 'A' for card in self.cards) and self.calculate_value() == 21
