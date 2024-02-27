# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:14:11 2024

@author: darko.velkov
"""


st = 'Print only the words that start with s in this sentence'
my_list = st.split()
my_list

for word in my_list:
    if word.startswith('s') and len(word)>1 :
        print(word)
    else:
        continue
    
    
    
    fuzz_list = list(range(1,100))
    fuzz_list
    
    for num in fuzz_list:
        if num%3==0 and num%5==0:
            print('FizzzBuzz')
        elif num%3==0:
            print('Fizz')
        elif num%5==0:
            print("Buzz")
            
        else:
            print(num)