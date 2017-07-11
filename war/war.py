class Card():
    suit_mapper = {
        'C': 'Clubs',
        'D': 'Diamonds',
        'H': 'Hearts',
        'S': 'Spades'
    }
    rank_mapper = {
        'J': 'Jack',
        'Q': 'Queen',
        'K': 'King',
        'A': 'Ace'
    }

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank if isinstance(rank, str) else str(rank)
        self.val = self.rank_value()

    def __str__(self):
        return '{} of {}'.format(Card.rank_mapper.get(self.rank, self.rank), Card.suit_mapper[self.suit])

    def __repr__(self):
        return 'Card({},{})'.format(self.rank, self.suit)



    def rank_value(self):
        cards = [str(i) for i in range(2, 11)] + [c for c in 'JQKA']
        return cards.index(self.rank)


class Deck():
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    suits = {'C', 'D', 'H', 'S'}

    def __init__(self, reset=True, ace_wrap=False):
        self.reset = reset
        self.ace_wrap = ace_wrap
        self.gather_cards()

    def __repr__(self):
        return 'Deck({},{})'.format(self.reset, self.ace_wrap)
    @property
    def __len__(self):
        return len(self.cards)
    def gather_cards(self):
        self.cards = [Card(rank, suit) for rank in Deck.ranks for suit in Deck.suits]

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hand_count=2, hand_size=26, shuffle=True):
        hands = []
        if self.reset or len(self.cards) < hand_size * hand_count:
            self.gather_cards()
        if shuffle:
            self.shuffle()
        for _ in range(hand_count):
            hands.append(self.cards[:hand_size])
            del self.cards[:hand_size]
        return hands
class Hand():
    def __init__(self, *cards):
        self.cards = cards



d = Deck()
h1, h2 = d.deal()
print(h1)
print(h2)