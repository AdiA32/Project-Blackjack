from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle


class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, clubs), (2, diamonds), (2, hearts), (2, spades), (3, clubs)]

    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, clubs), (Q, clubs), (10, clubs), (7, diamonds), (5, diamonds)]

    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, clubs)

    >>> d_hand = DealerHand()
    >>> deck.deal_hand(d_hand)
    >>> deck.deal_hand(d_hand)
    >>> print(d_hand)
    ____
    |Q  |
    | ♣ |
    |__Q|
    ____
    |?  |
    | ? |
    |__?|
    """

    # Class Attribute(s)

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        rank_list = list(range(2, 11)) + ["J", "Q", "K", "A"]
        suit_list = ["clubs", "diamonds", "hearts", "spades"]
        self.cards = [Card(rank, suit) for rank in rank_list for suit in suit_list]

    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        assert all(
            [
                isinstance(value, int) and value >= 0 and (key == "modified_overhand" or key == "mongean")
                for key, value in shuffle_and_count.items()
            ]
        )
        overhand_count = shuffle_and_count["modified_overhand"]
        mongean_count = shuffle_and_count["mongean"]
        self.cards = Shuffle.modified_overhand(self.cards, overhand_count)
        for i in range(mongean_count):
            self.cards = Shuffle.mongean(self.cards)

    def deal_hand(self, hand):
        """
        Takes the first card from the deck and adds it to `hand`.
        """
        assert isinstance(hand, PlayerHand)
        hand.add_card(self.cards.pop(0))

    def get_cards(self):
        return self.cards
