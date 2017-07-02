"""Sort a deck of cards."""


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank.

    >>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q',
    '7', 'J', '6', 'K'])
    ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    """
    if not cards:
        return cards
    list_of_cards = [
                    ['A', 0],
                    ['2', 0],
                    ['3', 0],
                    ['4', 0],
                    ['5', 0],
                    ['6', 0],
                    ['7', 0],
                    ['8', 0],
                    ['9', 0],
                    ['T', 0],
                    ['J', 0],
                    ['Q', 0],
                    ['K', 0]]
    for card in cards:
        for item in list_of_cards:
            if card == item[0]:
                item[1] += 1
    sorted_cards = []
    for card in list_of_cards:
        while card[1] != 0:
            sorted_cards.append(card[0])
            card[1] -= 1
    return sorted_cards


def sort_cards_pq(cards):
    """Sort shuffled list of cards, sorted by rank.

    >>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7',
    'J', '6', 'K'])
    ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    """
    if not cards:
        return cards
    sorted_list = []
    for card in cards:
        sorted_list = insert_card(card, sorted_list)
    return sorted_list


def insert_card(val, cards):
    """Add a card to the sorted list of cards."""
    list_of_cards = {
        'A': 0,
        '2': 1,
        '3': 2,
        '4': 3,
        '5': 4,
        '6': 5,
        '7': 6,
        '8': 7,
        '9': 8,
        'T': 9,
        'J': 10,
        'Q': 11,
        'K': 12
    }

    if len(cards) == 0:
        cards.append(val)
        return cards
    for i in range(len(cards)):
        if list_of_cards[cards[i]] > list_of_cards[val]:
            cards.insert(i, val)
            return cards
    cards.append(val)
    return cards
