# basic_strategy.py

from Blackjack.player import Player
from Blackjack.hand import Hand
from collections import defaultdict


class BasicStrategyPlayer(Player):
    """
    A class representing a blackjack player using basic strategy.

    Attributes
    ----------
    bankroll : int
        The amount of money the player has to bet with.
    min_bet : int
        The minimum amount the player can bet.
    hands : list
        A list of Hand objects representing the hands the player is currently playing.
    """

    # Surrender lookup table
    SURRENDER_LOOKUP = {
        16: defaultdict(lambda: False, {9: True, 10: True, 11: True}),
        15: defaultdict(lambda: False, {10: True})
    }

    # Split lookup table
    SPLIT_LOOKUP = {
        11: defaultdict(lambda: True),  # Always split aces
        10: defaultdict(lambda: False),  # Never split tens
        9: defaultdict(lambda: True, {7: False, 10: False, 11: False}),  # Split 9's against dealer 2-9, except 7
        8: defaultdict(lambda: True),  # Always split 8's
        7: defaultdict(lambda: False, {2: True, 3: True, 4: True, 5: True, 6: True, 7: True}),  # Split 7's against dealer 2-7
        6: defaultdict(lambda: False, {2: True, 3: True, 4: True, 5: True, 6: True}),  # Split 6's against dealer 2-6
        # Split 4's against dealer 5 and 6
        4: defaultdict(lambda: False, {5: True, 6: True}),
        # Split 3's and 2's against dealer 2-7
        3: defaultdict(lambda: False, {2: True, 3: True, 4: True, 5: True, 6: True, 7: True}),
        2: defaultdict(lambda: False, {2: True, 3: True, 4: True, 5: True, 6: True, 7: True}),
    }

    # Hard totals strategy
    HARD_TOTALS_LOOKUP = {
        21: defaultdict(lambda: "stand"),
        20: defaultdict(lambda: "stand"),
        19: defaultdict(lambda: "stand"),
        18: defaultdict(lambda: "stand"),
        17: defaultdict(lambda: "stand"),
        16: defaultdict(lambda: "hit", {2: "stand", 3: "stand", 4: "stand", 5: "stand", 6: "stand"}),
        15: defaultdict(lambda: "hit", {2: "stand", 3: "stand", 4: "stand", 5: "stand", 6: "stand"}),
        14: defaultdict(lambda: "hit", {2: "stand", 3: "stand", 4: "stand", 5: "stand", 6: "stand"}),
        13: defaultdict(lambda: "hit", {2: "stand", 3: "stand", 4: "stand", 5: "stand", 6: "stand"}),
        12: defaultdict(lambda: "hit", {4: "stand", 5: "stand", 6: "stand"}),
        11: defaultdict(lambda: "double"),
        10: defaultdict(lambda: "hit", {2: "double", 3: "double", 4: "double", 5: "double", 6: "double", 7: "double", 8: "double", 9: "double"}),
        9: defaultdict(lambda: "hit", {3: "double", 4: "double", 5: "double", 6: "double"}),
        8: defaultdict(lambda: "hit")
    }

    # Soft totals strategy
    SOFT_TOTALS_LOOKUP={
        20: defaultdict(lambda: "stand"),
        19: defaultdict(lambda: "stand", {6: "double"}),
        18: defaultdict(lambda: "hit", {2: "double", 3: "double", 4: "double", 5: "double", 6: "double", 7: "stand", 8: "stand"}),
        17: defaultdict(lambda: "hit", {3: "double", 4: "double", 5: "double", 6: "double"}),
        16: defaultdict(lambda: "hit", {4: "double", 5: "double", 6: "double"}),
        15: defaultdict(lambda: "hit", {4: "double", 5: "double", 6: "double"}),
        14: defaultdict(lambda: "hit", {5: "double", 6: "double"}),
        13: defaultdict(lambda: "hit", {5: "double", 6: "double"}),
    }



    def __init__(self, bankroll, min_bet):
        """
        Constructs all the necessary attributes for the basic strategy player object.

        Parameters
        ----------
            bankroll : int
                The amount of money the player has to bet with.
            min_bet : int
                The minimum amount the player can bet.
        """
        super().__init__(bankroll, min_bet)

    def decide_next_move(self, hand, dealer_card):
        """
        Decides the player's next move based on basic strategy.

        Parameters
        ----------
            hand : Hand
                The current hand the player is playing.
            dealer_card : Card
                The dealer's face-up card.

        Returns
        -------
        str
            The player's next move: 'H' for hit, 'S' for stand, 'D' for double if possible, 'P' for
            split, and 'U' for surrender.
        """

        # Check for surrender
        hand_value = hand.value()
        dealer_value = dealer_card.value
        if hand_value in self.SURRENDER_LOOKUP and self.SURRENDER_LOOKUP[hand_value][dealer_value]:
            return 'U' 

        # Check for split
        if hand.can_split and hand_value in self.SPLIT_LOOKUP and self.SPLIT_LOOKUP[hand_value][dealer_value]:
            return 'P'
        
        # Check if the hand is soft (contains an Ace counted as 11)
        is_soft = hand.is_soft()

        # Determine the move based on hard or soft totals
        if is_soft:
            # Check for soft totals strategy
            if hand_value in self.SOFT_TOTALS_LOOKUP:
                strategy = self.SOFT_TOTALS_LOOKUP[hand_value][dealer_value]
                if strategy == 'double':
                    return 'D' if hand.can_double else 'H'
                elif strategy == 'stand':
                    return 'S'
                elif strategy == 'hit':
                    return 'H'
        else:
            # Check for hard totals strategy
            if hand_value in self.HARD_TOTALS_LOOKUP:
                strategy = self.HARD_TOTALS_LOOKUP[hand_value][dealer_value]
                if strategy == 'double':
                    return 'D' if hand.can_double else 'H'
                elif strategy == 'stand':
                    return 'S'
                elif strategy == 'hit':
                    return 'H'

        # If no strategy fits, default to hit
        return 'H'