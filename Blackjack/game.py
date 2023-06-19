from Blackjack.dealer import Dealer
from Blackjack.shoe import Shoe
from Blackjack.player import Player
from Blackjack.strategies.basic_strategy import BasicStrategyPlayer

class Game:
    def __init__(self, num_decks, bankroll, betting_unit):
        """
        Initializes the game with the given number of decks, player's bankroll and betting unit.

        Parameters
        ----------
            num_decks : int
                The number of decks in the shoe.
            bankroll : int
                The player's initial bankroll.
            betting_unit : int
                The betting unit of the player.
        """
        self.shoe = Shoe(num_decks)
        self.player = Player(bankroll, betting_unit)
        self.dealer = Dealer()
        self.basic_strategy = BasicStrategyPlayer()
    
    def deal_initial_cards(self):
        """
        Deals two initial cards to the player and the dealer.
        """
        self.player.hand = [self.shoe.deal_card(), self.shoe.deal_card()]
        self.dealer.hand = [self.shoe.deal_card(), self.shoe.deal_card()]
    
    def play_player_hand(self):
        """
        Let the player play their hand based on the basic strategy until they stand or bust.
        """
        while True:
            dealer_card = self.dealer.hand[0]
            move = self.basic_strategy.decide_next_move(self.player.hand, dealer_card)
            
            if move == 'H':
                self.player.hand.append(self.shoe.deal_card())
            elif move == 'S':
                break
            # Handle other moves like 'D', 'P', 'U'
    
    def play_dealer_hand(self):
        """
        Let the dealer play their hand based on the dealer's rules until they stand or bust.
        """
        while self.dealer.should_hit():
            self.dealer.hand.append(self.shoe.deal_card())
    
    def resolve_bets(self):
        """
        Compare player's and dealer's hands to resolve bets.
        """
        # Compare self.player.hand to self.dealer.hand and update player's bankroll based on result
    
    def play_round(self):
        """
        Play a round of Blackjack.
        """
        if self.shoe.needs_shuffle():
            self.shoe.shuffle()
        
        # Reset hands
        self.player.hand = []
        self.dealer.hand = []
        
        # Deal initial cards
        self.deal_initial_cards()
        
        # Play player's hand
        self.play_player_hand()
        
        # Play dealer's hand
        self.play_dealer_hand()
        
        # Resolve bets
        self.resolve_bets()
    
    def start_game(self):
        """
        Start the game and keep playing rounds until the player decides to quit or runs out of money.
        """
        while True:
            self.play_round()
            
            # Check if the player wants to continue or has enough money
            # Prompt for user input, handle bankroll, etc.
