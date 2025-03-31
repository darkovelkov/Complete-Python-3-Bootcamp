#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 15:31:47 2025

@author: darko.velkov
"""

import PyPDF2

f = open('Working_Business_Proposal.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(f)
len(pdf_reader.pages)

page_one = pdf_reader.pages[0]
page_one_text = page_one.extract_text()
#page_one_text

pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(page_one)

pdf_output = open('Some_new.pdf','wb')

pdf_writer.write(pdf_output)
f.close()
pdf_output.close()