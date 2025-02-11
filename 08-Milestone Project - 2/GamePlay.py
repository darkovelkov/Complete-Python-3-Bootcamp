#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:07:46 2025

@author: darko.velkov
"""

from Deck import Deck
from Hand import Hand
from Chips import Chips

def take_bet(chips: Chips):
    
    while True:
        
        try:
            chips.bet = int(input("Please your bet please: "))
        except:
            print("Invalid value")
        else:
            if chips.bet > chips.total:
                print("Not enough money. You have {} chips left".format(chips.total))
            else:
                break
            
def hit(deck: Deck,hand: Hand):
    
    single_card=deck.deal_one()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    
def hit_or_stand(deck: Deck, hand: Hand):
    global playing
    
    while True:
        x = input("Hit or Stand? Please enter h or s: ")
        
        if x[0]=='h':
            hit(deck, hand)
        elif x[0]=='S':
            print("Player Stands! Dilers turn")
            playing=False
        else:
            print("I did not understand. Please enter valid value (h or s")
            continue
        break
    
def show_some(dealer: Hand,player: Hand):
    print("\n Dealer's hand: ")
    print("First hand is hidden")
    print(dealer.cards[1])
    
    print("\nPlayer's hand: ")
    for card in player.cards:
        print(card)
    
def show_all(dealer: Hand,player: Hand):
    print("\n Dealer's hand: ")
    for card in dealer.cards:
        print(card) 
    print(f"Dealer's value is: {dealer.value}") 
    print("\n Player's hand: ")
    for card in player.cards:
        print(card) 
    print(f"Player's value is: {player.value}")  
    
def player_busts(player: Hand, dealer: Hand, chips: Chips):
    print("Player Busts")
    chips.lose_bet()

def dealer_busts(player: Hand, dealer: Hand, chips: Chips):
    print("Dealer Busts")
    chips.win_bet()
    
def player_wins(player: Hand, dealer: Hand, chips: Chips):
    print("Player Busts")
    chips.win_bet()

def dealer_wins(player: Hand, dealer: Hand, chips: Chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player: Hand, dealer: Hand):
    print("Draw!")
    
    
    
while True:

    deck = Deck();
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())
    
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())
    
    player_chips=Chips(300)
    
    take_bet(player_chips)
    
    show_some(dealer_hand,player_hand)


    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
       

