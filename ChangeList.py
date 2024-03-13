#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:51:29 2024

@author: user
"""

def display(game_list):
    print("Here is the curent list: ")
    print(game_list)
    
def position_choice():
    choice = False
    while choice==False:
        position = input("Pick a position (0,1,2): ")
        if position in ["0","1","2"]:
            choice=True
            return int(position)
        else:
            print("Sorry invalid choice")

def replacement_choice(game_list,position):
    
    game_list[position] = input("Type a string to place at position: ")
    return game_list

def gameon_choice():
    choice = "wrong"
    while choice not in ["Y","N"]:
        choice = input("Keep playing? (Y,N): ")
        if choice not in ["Y","N"]:
            print("Sorry, I don't understand, please choose Y,N")
        if choice=="Y":
            return True
        else:
            return False
        
game_on = True
game_list = [0,1,2]


while game_on:
    display(game_list)
    position=position_choice()
    replacement_choice(game_list, position)
    display(game_list)
    gameon_choice()

    