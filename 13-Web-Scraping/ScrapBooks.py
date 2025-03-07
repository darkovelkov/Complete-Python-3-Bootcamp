#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:58:26 2025

@author: darko.velkov
"""

import requests
import bs4

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
paga_numer = 1

result = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(result.text,'lxml')
soup.select('.product_pod')

 