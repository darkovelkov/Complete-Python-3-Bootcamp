#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 14:49:23 2025

@author: darko.velkov
"""

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

from Deck import Deck

class Hand:
    
    def __init__(self):
        
        self.cards=[]
        self.value=0
        self.aces=0
        
    def add_card(self,card):
        
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank=='Ace':
            self.aces+=1
            
    def adjust_for_ace(self):
        
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1
                             

test_deck = Deck()
test_deck.shuffle()

test_player = Hand()
pulled_card=test_deck.deal_one()
print(pulled_card)
test_player.add_card(pulled_card)

print(test_player.value)