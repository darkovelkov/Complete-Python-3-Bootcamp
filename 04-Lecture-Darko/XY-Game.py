#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 23:14:43 2024

@author: Darko Velkov
"""

def printboard (row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
    
def userchoice():
    result=""
    listrange=range(0,11)
    while result not in listrange:
        result=input("Enter a value: (0,10)")    
        
        if result.isdigit()==False:
            print("Please enter digit")
        elif int(result) not in listrange:
            print("Enter digit between 0 and 10")
        else:
            return int(result) 
                
            
userchoice()
    