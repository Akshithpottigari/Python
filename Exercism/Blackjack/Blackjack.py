def value_of_card(card):
    """

    :param card: str - given card.
    :return: int - value of a given card (J, Q, K = 10, numerical value otherwise).
    """
    if card == 'K' or 'J' or 'Q':
        return 10
    else:
        return int(card)
    


def value_of_ace(hand_value):
    """

    :param hand_value: int - current hand value.
    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    if hand_value +11 > 21:
        return 1
    else:
        return 11
    


def is_blackjack(card_one, card_two):
    """

    :param card_one: str - first card in hand.
    :param card_two: str - second card in hand.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    if card_one =='A' and card_two !='A':
        blackjack = value_of_card(card_two) == 10
    elif card_one !="A" and card_two == "A":
        blackjack = value_of_card(card_one) == 10
    else:
        blackjack = False
    return blackjack


def can_split_pairs(card_one, card_two):
    """

    :param card_one: str - first card in hand.
    :param card_two: str - second card in hand.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    if card_one == "A" or card_two !="A":
        split_pairs = value_of_ace(card_one) == value_of_card(card_two)
    else:
        split_pairs = value_of_card(card_one) == value_of_card(card_two)
    return split_pairs        
    


def can_double_down(card_one, card_two):
    """

    :param card_one: str - first card in hand.
    :param card_two: str - second card in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """

    if card_one == 'A':
        card_one_value = 1
    else:
        card_one_value = value_of_card(card_one)

    if card_two == 'A':
        card_two_value = 1
    else:
        card_two_value = value_of_card(card_two)
    return 9<=(card_one_value+card_two_value)<=11