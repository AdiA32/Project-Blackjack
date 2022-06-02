class Shuffle:
    """
    Different kinds of shuffling techniques.

    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25]
    24

    >>> arr = Shuffle.modified_overhand([i for i in range(9)], 1)
    >>> arr
    [4, 0, 1, 2, 3, 5, 6, 7, 8]

    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25

    >>> Shuffle.mongean([i for i in range(1, 11)])
    [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]

    >>> Shuffle.mongean([i for i in range(1, 10)])
    [8, 6, 4, 2, 1, 3, 5, 7, 9]
    """

    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top.
        Then decrement `num` by 1 and continue the process till `num` = 0.
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """

        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        assert isinstance(cards, list) and isinstance(num, int)
        if num <= 0:
            return cards

        cards_even = len(cards) % 2 == 0
        num_even = num % 2 == 0

        if num == 1 and cards_even:
            middle = cards[len(cards) // 2 - 1]
            cards.remove(middle)
            return [middle] + cards

        start_i = (len(cards) // 2) - (num // 2)
        end_i = (len(cards) // 2) + (num // 2)
        if (cards_even and num_even) or (not cards_even and num_even):
            end_i -= 1

        middle_cards_list = cards[start_i: end_i + 1]
        for i in range(end_i, start_i - 1, -1):
            cards.pop(i)

        cards = middle_cards_list + cards
        return Shuffle.modified_overhand(cards, num - 1)

    def mongean(cards):
        """
        Implements the mongean shuffle.
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """

        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        # base cases
        if len(cards) == 1:
            return cards
        if len(cards) == 2:
            return cards[::-1]

        # recursion
        if len(cards) % 2 == 0:
            return [cards[-1]] + Shuffle.mongean(cards[:-2]) + [cards[-2]]
        else:
            return [cards[-2]] + Shuffle.mongean(cards[:-2]) + [cards[-1]]
