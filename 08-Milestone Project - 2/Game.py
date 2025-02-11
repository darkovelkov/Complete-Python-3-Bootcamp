#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 12:47:58 2025

@author: darko.velkov
"""

from Deck import Deck
from Player import Player


player_one = Player("Darko")
player_two = Player("Kike")
new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
#print(len(player_one.all_cards))

game_on = True

round_num = 0

while game_on:
    
    round_num +=1
    print(f'This is round {round_num}')
    
    if len(player_one.all_cards)==0:
        print("Player one is out of cards, Player two wins.")
        game_on=False
        break
    
    if len(player_two.all_cards)==0:
        print("Player two is out of cards, Player one wins.")
        game_on=False
        break    

player_one_cards=[]
player_one_cards.append(player_one.remove_one())

player_two_cards=[]
player_two_cards.append(player_two.remove_one())

at_war = True

while at_war:
    if player_one_cards[-1].value > player_two_cards[-1].value:
        player_one.add_cards(player_one_cards)
        player_one.add_cards(player_two_cards)
        
        at_war=False
        
        
    elif player_one_cards[-1].value < player_two_cards[-1].value:
        player_two.add_cards(player_one_cards)
        player_two.add_cards(player_two_cards)
        
        at_war=False



    else:
        print("WAR!")
        
        if len(player_one.all_cards)<5:
            print("Player Two Wins, not enough cards for WAR")
            game_on=False
            break
            
        elif len(player_two.all_cards)<5:
            print("Player Owo Wins, not enough cards for WAR")
            game_on=False
            break
        
        else:
            
            for x in range(5):
                player_one_cards.append(player_one.remove_one())
                player_two_cards.append(player_two.remove_one())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        