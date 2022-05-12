import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def cards_value(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value


deck = FrenchDeck()
for _ in range(5):
    card = choice(deck)
    print('Card rank: {}, card suit: {}, card_value: {}'
          .format(card.rank, card.suit, cards_value(card)))
