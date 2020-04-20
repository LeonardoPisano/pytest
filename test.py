#!/usr/bin/env python3.6

from functools import total_ordering
import random
from enum import IntEnum

class Deck(IntEnum):
    ONE = 1
    TWO = 2
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
    ACE = 14

class Suit(IntEnum):
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3
    CLUBS = 4

class DeckCard:
    def __init__(self, deck, suit):
        self.deck = deck
        self.suit = suit

    def __int__(self):
        return self.deck
        return self.suit

    def __str__(self):
        return "Карта: ({}, {})".format(self.deck, self.suit)

#Младшая карта
@total_ordering
def isMinor(_gt_):
    def _gt_(self,other):
        return self.int(card1.deck) > self.int(card2.deck)
    return isMinor(_gt_)

#Одна масть
@total_ordering
def sameSuit(_eq_):
    def _eq_(self,other):
        return self.card1.suit == self.card2.suit
    return sameSuit(_eq_)

#Первая карта бьёт вторую
def beats(isMinor, sameSuit):
    if (self.card1.suit == self.card2.suit) and (self.int(card1.deck) > self.int(card2.deck)):
        return
    else:
        return

#Первая карта бьёт вторую с учетом козыря
def beats2(beats, trump):
    if (self.trump.suit == self.card1.suit) and (self.trump.suit != self.card2.suit):
        return True

    elif (self.trump.suit == self.card2.suit) and (self.trump.suit != self.card1.suit):
        return False

    elif (self.trump.suit == self.card1.suit) and (self.trump.suit == self.card2.suit):
        return self.int(card1.deck) > self.int(card2.deck)

    return True

def random_card_factory():
    deck = random.choice(list(Deck))
    suit = random.choice(list(Suit))

    return DeckCard(deck, suit)

def main():
    card1 = random_card_factory()
    card2 = random_card_factory()
    trump = random.choice(list(Suit))
    print(trump)
    print(card1)
    print(card2)
    print('Первая карта младшая - {}'.format(int(card1.deck) < int(card2.deck)))
    print('Карты одной масти - {}'.format(card1.suit == card2.suit))
    print('Первая карта бьёт вторую - {}'.format((card1.suit == card2.suit) and (int(card1.deck) > int(card2.deck))))
    print('Первая козырная карта бьёт вторую - {}'.format((card1.suit == card2.suit) and (int(card1.deck) < int(card2.deck))))
    #print(beats2(beats, trump))

if __name__ == '__main__':
    main()
