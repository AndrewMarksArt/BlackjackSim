from Blackjack.deck import Deck
from Blackjack.card import Card
from Blackjack.hand import Hand
from Blackjack.player import Player
from Blackjack.dealer import Dealer
from Blackjack.game import BlackjackGame

def simple_strategy(dealer_up_card):
    # A very basic strategy for demonstration purposes
    return 'hit'

# Create a player with a bankroll of 1000 and a betting unit of 10
player = Player(bankroll=1000, betting_unit=10, strategy=simple_strategy)

# Create a dealer
dealer = Dealer()

# Initialize a game of Blackjack
game = BlackjackGame(player, dealer)

# Player places a bet
bet_amount = player.bet()
print(f"Player places a bet of {bet_amount}")
print(f"Player's bankroll before bet: {player.bankroll}")

# Deduct bet amount from player's bankroll
player.bankroll -= bet_amount
print(f"Player's bankroll after bet: {player.bankroll}")

# Deal the initial cards
game.deal_cards()

# Display the hands
print(f"Player's hand: {player.hand.cards[0]}, {player.hand.cards[1]}  (Value: {player.hand.calculate_value()})")
print(f"Dealer's hand: {dealer.hand.cards[0]}, {dealer.hand.cards[1]} (Value: {dealer.hand.calculate_value()})")

# Start player play_hand()
player.play_turn(dealer.hand.cards)

