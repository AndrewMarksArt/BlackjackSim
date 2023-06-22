from Blackjack.deck import Deck
from Blackjack.card import Card
from Blackjack.hand import Hand
from Blackjack.player import Player
from Blackjack.dealer import Dealer

class BlackjackGame:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.deck = Deck()
        self.deck.shuffle()

    def deal_cards(self):
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(self.deck.deal())
        player_hand.add_card(self.deck.deal())
        dealer_hand.add_card(self.deck.deal())
        dealer_hand.add_card(self.deck.deal())
        self.player.hand = player_hand
        self.dealer.hand = dealer_hand

    def play_hand(self):
        # Deal initial cards to player and dealer
        self.deal_cards()

        # player's turn

        # dealer's turn
        pass

    def check_for_winner(self):
        # Logic for checking the winner
        pass


    @property
    def deck(self):
        return self._deck

    @deck.setter
    def deck(self, deck):
        self._deck = deck
    