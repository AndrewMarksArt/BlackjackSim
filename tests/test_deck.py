import unittest
from Blackjack.deck import Deck

class TestDeck(unittest.TestCase):
    def test_deck(self):
        """
        This method tests the Deck class in the following ways:
        1) Ensures a new deck has 52 cards.
        """

        # Test that a new deck has 52 cards
        new_deck = Deck()
        self.assertEqual(len(new_deck.cards), 52, "New deck does not have 52 cards.")
        print("New deck card count test passed.")


if __name__ == '__main__':
    unittest.main()

