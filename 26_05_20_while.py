# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:53:18 2020

@author: marco
"""
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []
# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  < 17:
    hand.append(card_deck.pop())  
print(sum(hand))
print(hand)
