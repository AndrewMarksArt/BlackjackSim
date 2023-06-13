import unittest
from Blackjack.hand import Hand
from Blackjack.card import Card

class TestHand(unittest.TestCase):
    """
    Test suite for Hand class.
    We ensure that:
    1) A hand is initialized.
    2) Adding a card to the hand.
    3) Adjusting for Aces.
    4) Checking if a hand is bust.
    5) Checking for Blackjack.
    """

    def test_hand_initialization(self):
        """Test that hand is initialized with correct value and softness."""
        hand = Hand(Card('A', 'hearts'), Card('K', 'spades'))
        self.assertEqual(hand.value, 21, "Failed hand initialization, hand is initialized with a King and Ace and should sum to 21")
        print("Passed hand initialization test, a King and Ace sum to 21")
        self.assertTrue(hand.soft)
        print("Passed is soft test, any hand with an Ace and is less than or equal to 21 is soft")

    def test_hand_add_card(self):
        """Test that adding a card updates value and softness appropriately."""
        hand = Hand(Card('5', 'hearts'), Card('5', 'spades'))
        hand.add_card(Card('A', 'diamonds'))
        self.assertEqual(hand.value, 21, "Failed add card test, hand is initialized with two 5's and the next card is an Ace for a total of 21")
        print("Passed add card test, starting hand of two 5's value is 10, new card is an Ace with a value of 11, new total 21")
        self.assertTrue(hand.soft)
        print("Passed is soft test, any hand with an Ace and is less than or equal to 21 is soft")

    def test_hand_adjust_for_ace(self):
        """Test that ace adjustment works correctly when value exceeds 21."""
        hand = Hand(Card('A', 'hearts'), Card('K', 'spades'))
        hand.add_card(Card('K', 'diamonds'))
        self.assertEqual(hand.value, 21, "Failed adjust for Ace test, after card was added total was over 21 and there was an Ace so we subtract 10 from value")
        self.assertFalse(hand.soft)
        print("Passed is soft test, any hand with an Ace and over 21 the we subtract 10 from the value and set is_soft to False")

    def test_hand_is_bust(self):
        """Test that is_bust method works correctly."""
        hand = Hand(Card('K', 'hearts'), Card('K', 'spades'))
        hand.add_card(Card('2', 'diamonds'))
        self.assertTrue(hand.is_bust())
        print("Passed is_bust test, starting hand value is 20 and a 2 is added so total is over 21 and hand is bust")

    def test_hand_is_blackjack(self):
        """Test that is_blackjack method works correctly."""
        hand = Hand(Card('A', 'hearts'), Card('K', 'spades'))
        self.assertTrue(hand.is_blackjack())
        print("Passed is_blackjack test, had has 2 cards and total is 21")

if __name__ == '__main__':
    unittest.main()
