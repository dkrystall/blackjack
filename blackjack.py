from deck import Deck
from card import Suit, CardFace


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def indexAt(self, index):
        return self.items.index(index)


class Blackjack:

    def __init__(self, num_of_decks):
        self.playing_cards = Stack()
        for _ in range(0, num_of_decks):
            deck = Deck()
            deck.shuffle()
            for card in deck.cards:
                self.playing_cards.push(card)

    def deal_card(self):
        card = self.playing_cards.pop()
        return card


#game = Blackjack(5)
#card = game.deal_card()
#print(Suit(card.suit), CardFace(card.value))
#print(game.playing_cards.size())
#card2 = game.deal_card()
#print(Suit(card2.suit), CardFace(card2.value))
#print(game.playing_cards.size())
