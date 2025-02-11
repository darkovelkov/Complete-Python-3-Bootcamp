#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 23:44:21 2025

@author: velkovd@gmail.com
"""

class Dog():
    
    
    #Atributes
    #Take the argument
    #Assign to self.atrubute_name
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        
        
    
    def bark(self,number):
        print("WOOF! My name is {} and i am {} years old".format(self.name,number))

        
        
        
my_dog= Dog("Lab", "Tor4e")


type(my_dog)
my_dog.breed
my_dog.bark(10)