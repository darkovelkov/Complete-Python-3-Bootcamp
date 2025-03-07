#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:12:47 2025

@author: darko.velkov
"""
text='1234567-12345'
import re
text = "The agent's phone number phone is 1651856-16515. Call soon"

match = re.search("phone", text)

match.start()

#if there are multiple matches returns only the result of the first match so you need to use find all

matches = re.findall("phone", text)
matches

#for match in re.finditer("phone", text):
    #print(match.start())
 
phone=re.search(r'\d\d\d\d\d\d-\d\d\d\d\d', text)
phone

other_phone = re.search(r'\d{7}-\d{5}', text)
other_phone

phone_patter=re.compile(r'(\d{7})-(\d{5})')
results = re.search(phone_patter, text)
results.group(2)