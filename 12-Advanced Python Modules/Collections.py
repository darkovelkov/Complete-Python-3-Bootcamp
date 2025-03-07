#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:19:58 2025

@author: darko.velkov
"""

from collections import Counter
from collections import defaultdict
from collections import namedtuple

# counting all the unique letters in one word

word = 'Daaarrrrrrkooooooo'
s =Counter(word)

#This func from Counter will provide list of tupples as a result
s.most_common(2)

d1 = {'a' :2}
d1['a']

d = defaultdict(lambda:0)

d['pece']

#this is a tuple
var = (10,20,30)

a,b,c=var

#This is also a tuple
Dog = namedtuple('Dog',['age','name'])
sammy = Dog(age=5,name='Pece')
a,b = sammy
b
