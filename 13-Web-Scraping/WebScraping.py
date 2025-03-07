#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:45:18 2025

@author: darko.velkov
"""

import requests
import bs4

result = requests.get("https://example.com/")
type(result)
soup = bs4.BeautifulSoup(result.text,'lxml')
soup.select('title')

result_new = requests.get("https://en.wikipedia.org/wiki/Kobe_Bryant")
soup_new = bs4.BeautifulSoup(result_new.text,'lxml')
first_item = soup_new.select('.infobox-label')[0]
first_item.text

for item in soup_new.select('.infobox-label'):
    print(item.text)
    



    
