#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 20:29:19 2024

@author: user
"""

# This is a script for I/0 or writing and reading from a file

#myfile = open('file.txt', 'w')
#myfile.write('this is some text')
#myfile.close()

#test= open('file.txt' ,'r')
#content = test.read()
#print(content)

with open('/home/user/file.txt', mode='r') as f:
    print(f.readlines())
    s=[]
    s.append(0)
    s.append(0)
    s.append(0)
    print(s)