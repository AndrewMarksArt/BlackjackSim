import unittest
from Blackjack.card import Card
from Blackjack.player import Hand
from Blackjack.dealer import Dealer

class TestDealer(unittest.TestCase):
    """
    Unittest class for testing the Dealer class.
    """
    def setUp(self):
        """
        Set up method for each test. Here, we initialize the Dealer object.
        """
        self.dealer = Dealer()
        self.hand = Hand(Card('5', 'Hearts'), Card('6', 'Spades'))

    def test_decide_next_move(self):
        """
        Tests the decide_next_move method of the Dealer class.
        
        In this test, we create a hand for the dealer and test the 
        decide_next_move method for hand values that should result in a hit 
        and a stand.
        """
        # Test when hand value is less than 17, dealer should hit
        self.assertEqual(self.dealer.decide_next_move(self.hand), 'H', "Dealer should hit when hand value is less than 17.")
        print("Passed test for when dealers hand is less than 17 and the dealer needs to hit.")

        # Test when hand value is 17, dealer should stand
        self.hand.add_card(Card('6', 'Spades'))
        self.assertEqual(self.dealer.decide_next_move(self.hand), 'S', "Dealer should stand when hand value is 17 or more.")
        print("Passed test for when dealers hand is greater than or equal to 17 and the dealer needs to stand.")

if __name__ == '__main__':
    unittest.main()
