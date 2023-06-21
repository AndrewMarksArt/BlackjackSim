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
        dealer_up_value = 0
        if dealer_hand[0].value.isnumeric():
            dealer_up_value += int(dealer_hand[0].value)
        elif dealer_hand[0].value in ['J', 'Q', 'K']:
            dealer_up_value += 10
        elif dealer_hand[0].value == 'A':
            dealer_up_value += 11

        # Check if Dealer up card is an Ace
        if dealer_up_value == 11:
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

        # Check if the player should surrender
        player_hand_value = self.hand.calculate_value()
        if player_hand_value in Basic_Strategy.SURRENDER_LOOKUP:
            if Basic_Strategy.SURRENDER_LOOKUP[player_hand_value][dealer_up_value]:
                print("Player surrenders.")
                return 'surrender'
            else:
                print("Player doesn't surrender.")

        # Check if the player has a pair and should split
        if len(self.hand.cards) == 2 and self.hand.cards[0].value == self.hand.cards[1].value:
            print(f"player has a pair of {self.hand.cards[0].value}")
            if player_hand_value in Basic_Strategy.SPLIT_LOOKUP:
                if Basic_Strategy.SPLIT_LOOKUP[player_hand_value][dealer_up_value]:
                    print("Player splits their pair.")
                else:
                    print("Player does not split their pair.")


    def win(self, amount):
        self.bankroll += amount

    def lose(self, amount):
        self.bankroll -= amount
