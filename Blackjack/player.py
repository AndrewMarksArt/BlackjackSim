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

    def play_turn(self, dealer_hand):
        # Check Dealer up card value
        dealer_up_value = self.get_card_value(dealer_hand[0])

        # if dealer's face up card is an 'A' offer insurance
        self.offer_insurance(dealer_up_value)

        # Check if the player has a Blackjack
        if self.has_blackjack(self.hand):
            print("Player has Blackjack!")
            return 'blackjack'

        # Check if the player should surrender
        if self.should_surrender(self.hand, dealer_up_value):
            print("Player surrenders.")
            return 'surrender'

        # Check if the player has a pair and should split
        if self.should_split(self.hand, dealer_up_value):
            print("Player splits.")
        else:
            print("Player does not split.")
        


    def get_card_value(self, card):
        if card.value.isnumeric():
            return int(card.value)
        elif card.value in ['J', 'Q', 'K']:
            return 10
        elif card.value == 'A':
            return 11


    def offer_insurance(self, dealer_up_value):
        # Check if Dealer up card is an Ace
        if dealer_up_value == 11:
            print("Dealer offers players insurance.")
            if Basic_Strategy.TAKE_INSURANCE:
                print("player takes insurance.")
            else:
                print("player refused insurance.")


    def has_blackjack(self, hand):
        return len(hand.cards) == 2 and hand.calculate_value() == 21


    def should_surrender(self, hand, dealer_up_value):
        hand_value = hand.calculate_value()
        return hand_value in Basic_Strategy.SURRENDER_LOOKUP and Basic_Strategy.SURRENDER_LOOKUP[hand_value][dealer_up_value]

    
    def should_split(self, hand, dealer_up_value):
        if len(hand.cards) == 2 and hand.cards[0].value == hand.cards[1].value:
            hand_value = hand.calculate_value()
            return hand_value in Basic_Strategy.SPLIT_LOOKUP and Basic_Strategy.SPLIT_LOOKUP[hand_value][dealer_up_value]
        return False


    def win(self, amount):
        self.bankroll += amount

    def lose(self, amount):
        self.bankroll -= amount
