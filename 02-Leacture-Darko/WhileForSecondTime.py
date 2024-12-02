#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:12:07 2024

@author: user
"""

x=0
while x<5:
    print(f'The value of x is {x}')
    x=x+1
else:
    print('The value of x is now more than 4')
    
    
mystring= "Darko"
for letter in mystring:
    if letter=='o':
        break
    print(letter)
        