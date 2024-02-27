#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 22:28:04 2024

@author: user
"""

from random import randint
randomnNum = randint(0, 50)
 
#print(randomnNum)
while True:
    
    num = input("Pogodi go brojot Kike: ")
    number = int(num)
    if number>100 or number<0:
        print("Pomegju 0 i 100 da e ALOOOOO")
        
    elif number>randomnNum and number-randomnNum<10:
        print("Pomaaaal za malce")
            
    elif number<randomnNum and randomnNum-number<10:
        print("Pogooolem za malce")
           
    elif number<randomnNum and randomnNum-number>10:
        print("Pogooolem za mnoooogu")
           
    elif number>randomnNum and number-randomnNum>10:
        print("Pomaaaal za mnoooogu")
                        
    else:
        print("BRAVOOOOO KIKE")
        break