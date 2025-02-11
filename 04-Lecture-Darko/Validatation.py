#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:05:54 2024

@author: velkovd@gmail.com
"""

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


row=[' ',' ',' ']
row[1]='X'
display(row, row, row)


###result = int(input("Please enter a value: "))




def userchoice():
    choice = ""
    allowedrange = list(range(1,11))
    while choice.isdigit()==False or choice not in allowedrange:
        
        choice = input("Please enter digit (1-10): ")
        
        #Digit check
        if choice.isdigit()==False:
            print("Sorry that was not a digit")
        
        #Range check
        else:
            
            if int(choice) not in allowedrange:
                   print("Value not in range")
            else:       
                   return int(choice) 
          
                
                
userchoice()
            
            
        
        