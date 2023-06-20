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
    