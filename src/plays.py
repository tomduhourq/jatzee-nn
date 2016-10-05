NO_POSSIBLE_PLAY = "none"
STAIRS = "stairs"
FULL = "full"
POKER = "poker"
JATZEE = "jatzee"

plays = [NO_POSSIBLE_PLAY, STAIRS, FULL, POKER, JATZEE]

possible_numbers = [1, 2, 3, 4, 5, 6]
jatzee_hand_length = 5


def consequent_check(sorted_hand, last, x):
    return x == last or x + 1 == sorted_hand[sorted_hand.index(x) + 1]


def stairs(hand):
    """Checks if the hand passed by parameter has all distinct numbers and can be placed in order"""
    sorted_hand = sorted(hand)
    last = max(sorted_hand)
    return len(set(hand)) == jatzee_hand_length and \
           all(map(lambda x: consequent_check(sorted_hand, last, x), sorted_hand))


def full(hand):
    """Checks if the hand passed by parameter is a full hand (3 equal and 2 different)"""
    set_of_two = list(set(hand))
    return len(set_of_two) == 2 and (
        (len([number for number in hand if number == set_of_two[0]]) == 3 and len([number for number in hand if number == set_of_two[1]]) == 2) or
        (len([number for number in hand if number == set_of_two[0]]) == 2 and len([number for number in hand if number == set_of_two[1]]) == 3)
    )


def poker(hand):
    """Checks if the hand passed by parameter has 4 equal numbers and 1 distinct"""
    set_of_two = list(set(hand))
    return len(set_of_two) == 2 and (
        (len([number for number in hand if number == set_of_two[0]]) == 4 and len([number for number in hand if number == set_of_two[1]]) == 1) or
        (len([number for number in hand if number == set_of_two[0]]) == 1 and len([number for number in hand if number == set_of_two[1]]) == 4)
    )


def jatzee(hand):
    """Checks if all numbers in the hand are the same"""
    return len(set(hand)) == 1


def assert_stairs(hand):
    """Checks if the hand passed by parameter is a stairs hand (all different and subsequent)"""
    return assert_play(lambda numbers: stairs(numbers), STAIRS, hand)


def assert_full(hand):
    """Checks if the hand passed by parameter is a full hand (3 equal and 2 different)"""
    return assert_play(lambda numbers: full(numbers), FULL, hand)


def assert_poker(hand):
    """Checks if the hand passed by parameter is a poker hand (4 equal and 1 different)"""
    return assert_play(lambda numbers: poker(numbers), POKER, hand)


def assert_jatzee(hand):
    """Checks if the hand passed by parameter corresponds to a poker hand"""
    return assert_play(lambda numbers: jatzee(numbers), JATZEE, hand)


def assert_play(rule, name, hand):
    """
    Generic function to assert if the hand passed by parameter satisfies the rule,
    returning the value inside score array
    """
    if rule(hand):
        return plays.index(name)
    else:
        return plays.index(NO_POSSIBLE_PLAY)


def legal_hand(hand):
    """Checks if the hand corresponds to a jatzee hand"""
    return all(map(lambda x: x in possible_numbers, hand)) and len(hand) == jatzee_hand_length


def play(hand):
    """Checks if the hand is legal and returns which kind of play it was"""
    if legal_hand(hand):
        return plays[max([assert_stairs(hand), assert_full(hand), assert_poker(hand), assert_jatzee(hand)])]
    else:
        return "Illegal hand!"


