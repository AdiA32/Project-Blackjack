class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    False

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        assert rank in list(range(2, 11)) + ["A", "J", "Q", "K"]
        assert suit in ["hearts", "spades", "clubs", "diamonds"]
        assert isinstance(visible, bool)
        self.rank = rank
        self.suit = suit
        self.visible = visible

    def __lt__(self, other_card):
        rank_order = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        suit_order = ["clubs", "diamonds", "hearts", "spades"]
        if self.get_rank() != other_card.get_rank():
            return rank_order.index(self.get_rank()) < rank_order.index(other_card.get_rank())
        else:
            return suit_order.index(self.get_suit()) < suit_order.index(other_card.get_suit())

    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|
        """
        suit = {"hearts": "♥", "spades": "♠", "clubs": "♣", "diamonds": "♦"}
        if not self.visible:
            return "\n".join(["____", "|?  |", "| ? |", "|__?|"])
        return "\n".join(
            [
                "____",
                f"|{self.get_rank()}  |",
                f"| {suit[self.get_suit()]} |",
                f"|__{self.get_rank()}|",
            ]
        )

    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.
        """
        return f"({self.get_rank()}, {self.get_suit()})" if self.visible else "(?, ?)"

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def set_visible(self, visible):
        assert isinstance(visible, bool)
        self.visible = visible
