# pytest

#!/usr/bin/env python3.6

from functools import total_ordering
import random

class Card(object):
    def __init__(self, suits, decks):
        self.suits = suits
        self.decks = decks

    def __str__(self):
        return "Карта: ({}, {})".format(self.suits, self.decks)

    #Младшая карта
    @total_ordering
    def isMinor(_gt_):
        def _gt_(self,other):
            return self.decks.index(my_deck) > self.decks.index(you_deck)
        return

    #Одна масть
    @total_ordering
    def sameSuit(_eq_):
        def _eq_(self,other):
            return self.suits.index(my_suit) == self.suits.index(you_suit)
        return

    #Первая карта бьёт вторую
    def decks(isMinor, sameSuit):
        if (suits.index(my_suit) == suits.index(you_suit)) and (decks.index(my_deck) > decks.index(you_deck)):
            return
        else:
            return

    #Первая карта бьёт вторую козырную
    def beats2(beats):
        if (suits.index(my_suit) == suits.index(you_suit)) and (decks.index(my_deck) < decks.index(you_deck)):
            return
        else:
            return

    #Список карт бьющих козырную
    #def beatsList():


    #Сумма очков карт
    #def beatsList2():


suits = ["diamonds","hearts","spades","clubs"]
decks = ["six","seven","eight","nine","ten","jack","queen","king","ace"]

my_deck = random.choice(decks)
my_suit = random.choice(suits)

you_deck = random.choice(decks)
you_suit = random.choice(suits)

p1 = Card(my_deck, my_suit)
print(p1)

p2 = Card(you_deck, you_suit)
print(p2)


print('Первая карта младшая - {}'.format(decks.index(my_deck) > decks.index(you_deck)))

print('Карты одной масти - {}'.format(suits.index(my_suit) == suits.index(you_suit)))

print('Первая карта бьёт вторую - {}'.format((suits.index(my_suit) == suits.index(you_suit)) and (decks.index(my_deck) > decks.index(you_deck))))

print('Первая карта бьёт вторую козырнуюь - {}'.format((suits.index(my_suit) == suits.index(you_suit)) and (decks.index(my_deck) < decks.index(you_deck))))



