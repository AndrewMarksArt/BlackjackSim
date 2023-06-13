import unittest
from Blackjack.card import Card

class TestCard(unittest.TestCase):
    def test_card(self):
        # Test with a numeric card
        two_of_hearts = Card('2', 'hearts')
        self.assertEqual(two_of_hearts.value, 2, "2 card does not have the correct value.")
        print("2 card value test passed.")
        self.assertEqual(two_of_hearts.count_value, 1, "2 card does not have the correct count value.")
        print("2 card count value test passed.")

        # Test with a face card
        king_of_spades = Card('K', 'spades')
        self.assertEqual(king_of_spades.value, 10, "K card does not have the correct value.")
        print("K card value test passed.")
        self.assertEqual(king_of_spades.count_value, -1, "K card does not have the correct count value.")
        print("K card count value test passed.")

        # Test with an Ace
        ace_of_diamonds = Card('A', 'diamonds')
        self.assertEqual(ace_of_diamonds.value, 11, "A card does not have the correct value.")
        print("Ace card value test passed.")
        self.assertEqual(ace_of_diamonds.count_value, -1, "A card does not have the correct count value.")
        print("Ace card count value test passed.")

        # Test with a red seven
        seven_of_hearts = Card('7', 'hearts')
        self.assertEqual(seven_of_hearts.value, 7, "7 card does not have the correct value.")
        print("7 of hearts card value test passed.")
        self.assertEqual(seven_of_hearts.count_value, 1, "Red 7 card does not have the correct count value.")
        print("7 of hearts card count value test passed.")

        # Test with a black seven
        seven_of_spades = Card('7', 'spades')
        self.assertEqual(seven_of_spades.value, 7, "7 card does not have the correct value.")
        print("7 of spades card value test passed.")
        self.assertEqual(seven_of_spades.count_value, 0, "Black 7 card does not have the correct count value.")
        print("7 of spades card count value test passed.")


if __name__ == '__main__':
    unittest.main()
