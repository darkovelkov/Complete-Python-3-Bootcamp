#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 18:42:50 2025

@author: darko.velkov
"""

import csv
import PyPDF2
import re


f = open('find_the_link.csv', 'r')
csv_data = csv.reader(f)

data_lines = list(csv_data)
link=''
for row_num,data in enumerate(data_lines):
    link += data[row_num]
    
link

f_pdf = open('Find_the_Phone_Number.pdf','rb')
pdf_reader = PyPDF2.PdfReader(f_pdf)
all_text = ''
pattern = r'\d{3}.\d{3}.\d{4}' 
for n in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[n]
    page_text = page.extract_text()
    all_text = all_text+' '+page_text
    
for match in re.findall(pattern, all_text):
    print(match)
    