#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 01:41:44 2024

@author: velkovd@gmail.com
"""

samplelist = ['0','1','2']

def displaylist(gamelist):
    print(gamelist)
    
#displaylist(samplelist)    

def positionchoice():
    position='Wrong'
    
    while position not in ['0','1','2']:
        position = input ("Please enter a position: ")
        if position not in ['0','1','2']:
            print("Please enter valid position")
    return int(position)       

#positionchoice()

def replacementchoice(gamelist,position):
    
    newvalue = input("Please enter replacement string: ")
    gamelist[position]=newvalue
    
def gameon_choice():
    value='Wrong'
    
    while value not in ['Y', 'N']:
        value=input("Do you whant to keep playing? (Y,N) ")
        if value not in ['Y', 'N']:
            print("Please enter valid (Y,N)")
        
        else:
            return False
        
    return True

#gameon_choice()        

gamelist = ['1','2','3']
game_on=True


while game_on:
    displaylist(gamelist)
    position = positionchoice()
    replacementchoice(gamelist, position)
    displaylist(gamelist)
    game_on = gameon_choice()