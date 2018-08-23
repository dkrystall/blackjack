from card import Suit, CardFace, Card
from random import shuffle


class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(1, (len(list(Suit))+1)):
            for value in range(1, (len(list(CardFace))+1)):
                self.cards.append(Card(suit, value))
        print "Cards in this deck:", len(self.cards)

    def shuffle(self):
        shuffle(self.cards)
        print "Shuffling..."
