from collections import defaultdict


class Basic_Strategy():

    # Take insurance logic
    TAKE_INSURANCE = False

    # Surrender lookup table
    SURRENDER_LOOKUP = {
        16: defaultdict(lambda: False, {9: True, 10: True, 11: True}),
        15: defaultdict(lambda: False, {10: True})
    }

    # Split lookup table
    SPLIT_LOOKUP = {
        # we calculate hand value by adding the value of both cards and adjusting for 'A's
        12: defaultdict(lambda: True),  # Always split aces, a pair of A's will total 11+1 for 12
        20: defaultdict(lambda: False),  # Never split tens
        18: defaultdict(lambda: True, {7: False, 10: False, 11: False}),  # Split 9's against dealer 2-9, except 7
        16: defaultdict(lambda: True),  # Always split 8's
        14: defaultdict(lambda: False, {2: True, 3: True, 4: True, 5: True, 6: True, 7: True}),  # Split 7's against dealer 2-7
        12: defaultdict(lambda: False, {2: True, 3: True, 4: True, 5: True, 6: True}),  # Split 6's against dealer 2-6
        # Split 4's against dealer 5 and 6
        8: defaultdict(lambda: False, {5: True, 6: True}),
        # Split 3's and 2's against dealer 2-7
        6: defaultdict(lambda: False, {2: True, 3: True, 4: True, 5: True, 6: True, 7: True}),
        4: defaultdict(lambda: False, {2: True, 3: True, 4: True, 5: True, 6: True, 7: True}),
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
