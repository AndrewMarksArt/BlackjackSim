from Blackjack.strategies.basic import Basic_Strategy
from Blackjack.hand import Hand
from Blackjack.card import Card

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

    def play_turn(self, dealer_hand, deck):
        # Get dealer card values
        dealer_up_value = self.get_card_value(dealer_hand[0])
        dealer_total = dealer_up_value + self.get_card_value(dealer_hand[1])

        # if dealer's face up card is an 'A' offer insurance
        self.offer_insurance(dealer_up_value)

        if dealer_total == 21:
            print("Dealer has Blackjack")
            return 'dealer blackjack', self.hand.calculate_value()

        # Check if the player has a Blackjack
        if self.has_blackjack(self.hand):
            print("Player has Blackjack!")
            return 'blackjack', self.hand.calculate_value()

        # Check if the player should surrender
        if self.should_surrender(self.hand, dealer_up_value):
            print("Player surrenders.")
            return 'surrender', self.hand.calculate_value()

        # Check if the player has a pair and should split
        if self.should_split(self.hand, dealer_up_value):
            print("Player splits.")
            # split hand into two hands
            hand1, hand2 = self.split_hand(self.hand)
            # deal card to first hand only, after this hand is resolved, deal second hand
            hand1.add_card(deck.deal())
            print(f"Player hand 1: {hand1.cards[0]}, {hand1.cards[1]}")

            # Next action for hand 1
            #
            #

            # check if new hand is a pair
            if self.should_split(hand1, dealer_up_value):
                print("player splits, again")
                hand1, hand3 = self.split_hand(hand1)
                
                # deal new card to hand 1
                hand1.add_card(deck.deal())

                # check to see if the new hand is a pair
                if self.should_split(hand1, dealer_up_value):
                    # split to create 4 hands, player can no longer split
                    print("Player splits again and cannot split any more.")
                    hand1, hand4 = self.split_hand(hand1)

                    hand1.add_card(deck.deal())


                else:
                    # play hand 1, then deal and play hand 2, then deal and play hand 3
                    pass

            else:
                # hand 1 is ready to play, once that hand is finished deal cards to hand 2
                pass
    
        else:
            print("Player does not split.")

            while self.hand.calculate_value() < 21:
                next_move = self.next_action(self.hand, dealer_up_value)
                print(next_move)
                if next_move == 'hit':
                    self.hit(deck)
                elif next_move == 'double':
                    self.hit(deck)
                    return 'double', self.hand.calculate_value()
                    # player hand done, calculate final hand value and move to dealers turn
                    #
                    #

                else:
                    print("Players Final Hand")
                    for i in range(len(self.hand.cards)):
                        print(f"{self.hand.cards[i]}")
                    print(f"Players total:({self.hand.calculate_value()}) vs Dealers up card {dealer_up_value}")
                    return 'stand', self.hand.calculate_value()
            
            if self.hand.calculate_value() > 21:
                print("Player is Bust.")
                for i in range(len(self.hand.cards)):
                        print(f"{self.hand.cards[i]}")
                print(f"Players total:({self.hand.calculate_value()}) vs Dealers up card {dealer_up_value}")
                return 'bust', self.hand.calculate_value()

            elif self.hand.calculate_value() == 21:
                print("Player has 21 and stands.")
                for i in range(len(self.hand.cards)):
                        print(f"{self.hand.cards[i]}")
                print(f"Players total:({self.hand.calculate_value()}) vs Dealers up card {dealer_up_value}")
                return 'stand', self.hand.calculate_value()

    def get_card_value(self, card):
        """
        convert the value of a card to an int
        """
        if card.value.isnumeric():
            return int(card.value)
        elif card.value in ['J', 'Q', 'K']:
            return 10
        elif card.value == 'A':
            return 11


    def offer_insurance(self, dealer_up_value):
        """
        check if the dealers face up card is an 'A' and offer the player insurance
        check strategy to see if the player wants to take insurance.
        """
        # Check if Dealer up card is an Ace
        if dealer_up_value == 11:
            print("Dealer offers players insurance.")
            if Basic_Strategy.TAKE_INSURANCE:
                print("player takes insurance.")
            else:
                print("player refused insurance.")



    def has_blackjack(self, hand):
        """
        check if the player has blackjack.
        """
        return len(hand.cards) == 2 and hand.calculate_value() == 21


    def should_surrender(self, hand, dealer_up_value):
        """
        check if the player should surrender based on players hand value and dealers face up card value and
        action in loopup table.
        """
        if hand.is_soft():
            pass
        else:
            hand_value = hand.calculate_value()
            return hand_value in Basic_Strategy.SURRENDER_LOOKUP and Basic_Strategy.SURRENDER_LOOKUP[hand_value][dealer_up_value]

    
    def should_split(self, hand, dealer_up_value):
        """
        check if the player has a pair, look up if the player should split from the strategy table.
        """
        if len(hand.cards) == 2 and hand.cards[0].value == hand.cards[1].value:
            hand_value = hand.calculate_value()
            return hand_value in Basic_Strategy.SPLIT_LOOKUP and Basic_Strategy.SPLIT_LOOKUP[hand_value][dealer_up_value]
        return False

    def next_action(self, hand, dealer_up_card):
        """
        Use lookup table to see what the players next action should be
        """
        hand_value = hand.calculate_value()
        if hand.is_soft() and len(hand.cards) == 2:
            print("Player's hand is soft, using the soft totals lookup table.")
            return hand_value in Basic_Strategy.SOFT_TOTALS_LOOKUP and Basic_Strategy.SOFT_TOTALS_LOOKUP[hand_value][dealer_up_card]
        else:
            return hand_value in Basic_Strategy.HARD_TOTALS_LOOKUP and Basic_Strategy.HARD_TOTALS_LOOKUP[hand_value][dealer_up_card]


    def hit(self, deck):
        """
        If action is 'hit', deal 1 card from the deck to the hand
        """
        self.hand.add_card(deck.deal())


    def split_hand(self, hand):
        # create two new hands
        hand1 = Hand()
        hand2 = Hand()

        # add one card from the original hand into the new hands
        hand1.add_card(hand.cards[0])
        hand2.add_card(hand.cards[1])

        # return the two new hands
        return hand1, hand2


    def win(self, amount):
        self.bankroll += amount

    def lose(self, amount):
        self.bankroll -= amount
