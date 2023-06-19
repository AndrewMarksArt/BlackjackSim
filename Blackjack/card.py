class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
        return f"{self.value} of {self.suit}"

