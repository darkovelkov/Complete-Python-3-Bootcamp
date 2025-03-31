#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 14:57:44 2025

@author: darko.velkov
"""

import csv

data = open("example.csv", encoding='utf-8')

csv_data = csv.reader(data)

data_lines=list(csv_data)

all_emails=[]

for line in data_lines[1:5]:
    all_emails.append(line[3])
    
    
all_emails

full_names = []

for line in data_lines[1:5]:
    full_names.append(line[1] + " " + line[2])    

full_names