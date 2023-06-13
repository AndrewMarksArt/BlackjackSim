import unittest
from Blackjack.shoe import Shoe

class TestShoe(unittest.TestCase):
    def setUp(self):
        """
        Set up a shoe object for each test.
        """
        self.one_deck_shoe = Shoe(1)
        self.six_deck_shoe = Shoe(6)

    def test_shoe_creation(self):
        """
        Test that a shoe is created with the correct number of cards.
        """
        self.assertEqual(len(self.one_deck_shoe.cards), 52, "Single deck shoe creation and length failed.")
        self.assertEqual(len(self.six_deck_shoe.cards), 52*6, "Six deck shoe creation and length failed.")
        print("Deck creation and length tests passed.")

    def test_shoe_shuffle(self):
        """
        Test that the shoe can be shuffled.
        """
        original_order = self.one_deck_shoe.cards.copy()
        self.one_deck_shoe.shuffle()
        self.assertNotEqual(self.one_deck_shoe.cards, original_order, "Shoe shuffle test failed.")
        print("Shoe shuffle test passed.")

    def test_deal_card(self):
        """
        Test that a card can be dealt from the shoe.
        """
        print("test dealing cards.")
        initial_length = len(self.one_deck_shoe.cards)
        card = self.one_deck_shoe.deal_card()
        self.assertEqual(len(self.one_deck_shoe.cards), initial_length - 1, "Deal card test failed, shoe length does not decrease.")
        self.assertNotIn(card, self.one_deck_shoe.cards, "Deal card test failed, card that was dealt is still in the shoe.")
        print("Deal card tests passed.")

    def test_needs_shuffle(self):
        """
        Test that needs_shuffle works correctly.
        """
        self.assertFalse(self.one_deck_shoe.needs_shuffle())
        print("Full shoe test passed.")
        print("deal cards till we hit the cut card")
        for _ in range(int(0.75 * 52)+1):
            self.one_deck_shoe.deal_card()
        print("cut card hit")
        self.assertTrue(self.one_deck_shoe.needs_shuffle())
        print("Needs shuffle test passed")
        

if __name__ == '__main__':
    unittest.main()
