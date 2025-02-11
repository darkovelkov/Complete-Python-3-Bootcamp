#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:02:49 2025

@author: darko.velkov
"""

class Chips:
    
    def __init__(self, total=100):
        self.total=total
        self.bet = 0
        
    def win_bet(self):
        self.total +=self.bet
        
    def lose_bet(self):
        self.total-=self.bet

