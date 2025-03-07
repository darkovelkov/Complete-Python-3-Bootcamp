#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:53:55 2025

@author: darko.velkov
"""

import os 
import shutil
import send2trash
os.getcwd()
os.listdir('/home/user')

#This is how you can move a file (replace source and destination)
#shutil.move("src", "dst")

#send2trash.send2trash("Darko.txt")

file_path = '/home/user/projects/Python/Python-GH/Complete-Python-3-Bootcamp/12-Advanced Python Modules/Example_Top_Level'
os.walk(file_path)

for folder,sub_folders,files in os.walk(file_path):
    print (f"Curuently looking at {folder}")    
    print('\n')
    print ("The Sub folder are: ") 
    for sub_folder in sub_folders:
        print (f"This are subfolders {sub_folder}")
    print('\n')
    print ("This are the folders: ")
    print('\n')
    for f in files:
        f = open(f,'w+')
        f.read()
        print(f'This are the files: {f}')
        print('\n')
