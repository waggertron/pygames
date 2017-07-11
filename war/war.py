class Card:
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

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def rank_value(self):
        cards = [str(i) for i in range(2, 11)] + [c for c in 'JQKA']
        return cards.index(self.rank)


class Deck:
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    suits = {'C', 'D', 'H', 'S'}

    def __init__(self, reset=True, ace_wrap=False):
        self.reset = reset
        self.ace_wrap = ace_wrap
        self.gather_cards()

    def __repr__(self):
        return 'Deck({},{})'.format(self.reset, self.ace_wrap)

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
            hands.append(Hand(self.cards[:hand_size]))
            del self.cards[:hand_size]
        return hands


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __len__(self):
        return len(self.cards)

    def draw(self):
        return self.cards.pop()

    def take(self, cards):
        if isinstance(cards, tuple):
            cards = list(cards)
        self.cards = cards + self.cards


def war(h1,h2, cards):
    print('WAR HAS BEEN DECLARED')
    try:
        for i in range(3):
            card1 = h1.draw()
            card2 = h2.draw()
            cards.append(card1)
            cards.append(card2)
    except:
        return {"winner": 'h1', "gameover": True} if len(h2) == 0 else {"winner": 'h2', "gameover": True}
    card1, card2 = h1.draw(), h2.draw()
    cards.append(card1)
    cards.append(card2)
    if card1 > card2:
        return {
            'winner': h1,
            'cards': cards
        }
    elif card2 > card1:
        return {
            'winner': h2,
            'cards': cards
        }
    else:
        return war(h1, h2, cards)




def game():
    deck = Deck()
    h1,h2 = deck.deal()
    while len(h1) > 0 and len(h2) > 0:
        cards = [h1.draw(), h2.draw()]
        card1, card2 = cards
        print('{} vs. {}'.format(card1, card2))
        if card1 > card2:
            h1.take(cards)
        elif card1 < card2:
            h2.take(cards)
        else:
            result = war(h1, h2, cards)
            if result.get('gameover', False):
                print('winner is {}'.format(result['winner']))
                import sys
                sys.exit()
            else:
                result['winner'].take(result['cards'])
        print('h1 has: {} cards\nh2 has: {} cards'.format(len(h1), len(h2)))






game()