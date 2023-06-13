import unittest
from Blackjack.player import Player
from Blackjack.hand import Hand
from Blackjack.card import Card

class TestPlayer(unittest.TestCase):
    """
    A class to test the functionality of the Player class.
    """

    def setUp(self):
        """
        Set up a Player instance and a Hand instance for the tests.
        """
        self.player = Player(1000, 50)
        self.hand = Hand(Card('A', 'Hearts'), Card('K', 'Spades'))

    def test_init(self):
        """
        Test whether the Player instance is initialized with the right attributes.
        """
        self.assertEqual(self.player.bankroll, 1000, "The bankroll was not initialized correctly.")
        self.assertEqual(self.player.min_bet, 50, "The minimum bet was not initialized correctly.")
        self.assertEqual(self.player.hands, [], "The hands list was not initialized correctly.")
        print("Passed player initialization test.")

    def test_deal_hand(self):
        """
        Test whether a Hand can be correctly dealt to the Player.
        """
        self.player.deal_hand(Card('A', 'Hearts'), Card('K', 'Spades'))
        self.assertEqual(len(self.player.hands), 1, "The hand was not dealt correctly.")
        self.assertEqual(self.player.hands[0].cards[0].rank, 'A', "The first card was not dealt correctly.")
        self.assertEqual(self.player.hands[0].cards[1].rank, 'K', "The second card was not dealt correctly.")
        print("Passed dealing a hand to the player test.")

    def test_place_bet(self):
        """
        Test whether a bet can be correctly placed by the Player.
        """
        bet = self.player.place_bet()
        self.assertEqual(bet, 50, "The bet amount is incorrect.")
        self.assertEqual(self.player.bankroll, 950, "The bankroll was not decreased correctly after the bet.")
        print("Passed placing a bet test, bet was placed and bankroll was deducted buy the bet amount.")

    def test_receive_winnings(self):
        """
        Test whether winnings can be correctly received by the Player.
        """
        self.player.receive_winnings(100)
        self.assertEqual(self.player.bankroll, 1100, "The bankroll was not increased correctly after receiving winnings.")
        print("Passed receiving winnings test, bankroll increased by amount won.")

    def test_can_split(self):
        """
        Test whether it can be correctly determined whether a hand can be split.
        """
        self.player.deal_hand(Card('A', 'Hearts'), Card('A', 'Spades'))
        self.assertTrue(self.player.can_split(self.player.hands[0]), "The method incorrectly indicated that a hand of two aces can't be split.")
        self.player.deal_hand(Card('A', 'Hearts'), Card('K', 'Spades'))
        self.assertFalse(self.player.can_split(self.player.hands[1]), "The method incorrectly indicated that a hand of Ace and King can be split.")
        print("Passed if hand can be split tests, correctly indicates a hand of 2 Aces can be split and a hand of Ace King cannot be split.")

    def test_reset(self):
        """
        Test whether the Player can be correctly reset.
        """
        self.player.deal_hand(Card('A', 'Hearts'), Card('K', 'Spades'))
        self.player.reset()
        self.assertEqual(self.player.hands, [], "The Player was not reset correctly.")
        print("Passed resetting the Players hand test, resets the hand to an empty list.")

if __name__ == '__main__':
    unittest.main()
