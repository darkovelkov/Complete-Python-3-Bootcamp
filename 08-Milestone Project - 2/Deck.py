#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:24:55 2025

@author: darko.velkov
"""
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


from Card import Card
import random
class Deck:
    
    def __init__(self):
        
        self.all_cards =  []
        
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit, rank)
                self.all_cards.append(created_card)


    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def __str__(self):
        deck_comp=''
        for card in self.all_cards:
            deck_comp+='\n'+card.__str__()
        return "The deck has: " + deck_comp
        
    def deal_one(self):
        return self.all_cards.pop()
    
        


