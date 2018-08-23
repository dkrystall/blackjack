from enum import Enum
from collections import namedtuple


class Suit(Enum):
    SPADE = 1
    CLUB = 2
    DIAMOND = 3
    HEART = 4


class CardFace(Enum):
    ACE = 1
    DEUS = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


Card = namedtuple("Card", "suit value")
