#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 23:33:17 2025

@author: darko.velkov
"""

import shutil
import os
import re

dir_to_unzip = '/home/user/projects/Python/Python-GH/Complete-Python-3-Bootcamp/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise/'
file_name = 'unzip_me_for_instructions.zip'
#shutil.unpack_archive(dir_to_unzip+file_name,'unziped','zip')
top_dir = '/home/user/projects/Python/Python-GH/Complete-Python-3-Bootcamp/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise/extracted_content'
for folders,sub_folders,files in os.walk(top_dir):
    print(f'You are currently in this folder: {folders}')
    print('\n')
    print('The SUBLODERS ARE: ')
    for sub_folder in sub_folders:
        print(f'SUBFOLDER {sub_folder}')
    print('\n')
    print('THE FILES ARE: ')
    for file in files:
        file = open(file,'w+')
        file_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
        content = file.read()
        print(content)
        result=re.search(file_pattern, content)
        print(result)
        print(f'FILES: {file}')
    