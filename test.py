#! /usr/bin/env python3.6

from enum import IntEnum
import random
from functools import total_ordering

class Card(IntEnum):
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

@total_ordering
class DeckCard:
    def __init__(self, card, suit):
        self.card = card
        self.suit = suit

    def __int__(self):
        return self.card

    def __lt__(self, other):
        return self.card < other.card

    #def __gt__(self, other):
        #return ('QWE {} {}'.format(self.card > other.card))

    def __eq__(self, other):
        return self.card == other.card

    def __repr__(self):
        suit = dict()
        suit[1] = 'diamonds'
        suit[2] = 'hearts'
        suit[3] = 'spades'
        suit[4] = 'clubs'

        card = dict()
        card[1] = 'one'
        card[2] = 'two'
        card[3] = 'three'
        card[4] = 'four'
        card[5] = 'five'
        card[6] = 'six'
        card[7] = 'seven'
        card[8] = 'eight'
        card[9] = 'nine'
        card[10] = 'ten'
        card[11] = 'jack'
        card[12] = 'queen'
        card[13] = 'king'
        card[14] = 'ace'

        return '{} {}'.format(suit[int(self.suit)], card[int(self)])

    def isMinor(self):
        return int(self.card) <= 10


def random_card_factory():
    card = random.choice(list(Card))
    suit = random.choice(list(Suit))

    return DeckCard(card, suit)

def yes_no(result):
    if result:
        return "бьёт"
    return "не бьёт"

def sameSuit(card1, card2):
    return card1.suit == card2.suit

def beats(card1, card2):
    if (int(card1) > int(card2)) and (card1.suit == card2.suit):
        return True
    return False

def beats2(beats, card1, card2, trump):
    if (card1.suit == trump) and (beats == True):
        return True
    elif (card1.suit == trump) and (card1.suit != card2.suit):
        return True
    elif (beats == True):
        return True
    return False
    #if card1.suit == trump:
        #return True

def beatsList(beatlist, card2, trump):
    winning_card_list = list()

    for card in beatlist:
        if beats2(card, card2, trump):
            winning_card_list.append(card)

    return winning_card_list

class Play:
    def __init__(self):
        self.card1 = random_card_factory()
        self.card2 = random_card_factory()

    def run(self):
        print(self.card1)
        print(self.card2)

        print('Младшая карта {}'.format(self.card1.isMinor()))

        same_suit_result = sameSuit(self.card1, self.card2)
        print('Карты одной масти {}'.format(same_suit_result))

        beats_result = yes_no(beats(self.card1, self.card2))
        print('Карта {} {} карту {}'.format(self.card1, beats_result, self.card2))
        #print('Карта {} {} карт {}'.format(card1, yes_no(beats(card1, card2)), card2))

        beats2_result = yes_no(beats2(beats(self.card1, self.card2), self.card1, self.card2, Suit.SPADES))
        print('Карта {} {} карту {}'.format(self.card1, beats2_result, self.card2))
        #print(a.beatsList(beatlist, card2, Suit.SPADES))


def main():
    game = Play()
    game.run()

if __name__ == '__main__':
    main()

