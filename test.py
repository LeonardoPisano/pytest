#!/usr/bin/env python3.6

#six        suit - масть
#seven      deck - колода
#eight      trump - козырь
#nine
#ten
#eleven - jack      diamonds - бубны
#twelve - queen     hearts - черви
#thirteen - king    spades - пики
#fourteen - ace     clubs - крести

from enum import IntEnum
import random
from functools import total_ordering
from functools import reduce
import functools

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
        return int(self.card)

    def __lt__(self, other):
        return self.card < other.card

    def __eq__(self, other):
        return self.card == other.card

    def __add__(self, other):
        return self.card + other.card

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


def q(card1, card2):
    return int(card1) + int(card2)

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

def beats2(card1, card2, trump):
    if_beats = beats(card1, card2)

    if (card1.suit == trump) and (if_beats == True):
        return True
    elif (card1.suit == trump) and (card1.suit != card2.suit):
        return True
    elif (if_beats == True):
        return True
    return False


def beatsList(beatlist, card2, trump):
    mapping_result = list(map(lambda x: x if beats2(x, card2, trump) else False, beatlist))
    winning_card_list = list(filter(lambda x: x, mapping_result))

    return winning_card_list

def custom_sum(first, second):
    return first + second


def qwe(li):
    lis = list()
    for card in li:
        if int(card) == int(card):
            lis.append(reduce(lambda x, y: x+y, li))
    return lis


class Play:
    def __init__(self):
        self.card1 = random_card_factory()
        self.card2 = random_card_factory()

    def run(self):
        print(self.card1)
        print(self.card2)

        #print(self.card1.__eq__(self.card2))
        #print(self.card1 == self.card2)
        #print(self.card1.__lt__(self.card2))
        #print(self.card1 < self.card2)

        numbers = [3, 4, 6, 9, 34, 12]
        print(numbers)

        random_card_list = [random_card_factory() for x in range(0,10)]
        print(random_card_list)

        random_card_list1 = [random_card_factory() for x in range(0,3)]
        print(random_card_list1)

        print('Младшая карта {}'.format(self.card1.isMinor()))

        q_r = q(self.card1, self.card2)
        print(q_r)
        
        same_suit_result = sameSuit(self.card1, self.card2)
        print('Карты одной масти {}'.format(same_suit_result))

        beats_result = yes_no(beats(self.card1, self.card2))
        print('Карта {} {} карту {}'.format(self.card1, beats_result, self.card2))

        beats2_result = yes_no(beats2(self.card1, self.card2, Suit.SPADES))
        print('Карта {} {} карту {}'.format(self.card1, beats2_result, self.card2))

        print(beatsList(random_card_list, self.card2, Suit.SPADES))

        #!!print(qwe(random_card_list1))
        result = reduce(custom_sum, numbers)
        print(result)

def func():
    game = Play()
    game.run()

def higher_order_function(func_param):
    func_param()

def main():
    higher_order_function(func)

if __name__ == '__main__':
    main()
