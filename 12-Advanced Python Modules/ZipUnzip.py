#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 23:16:19 2025

@author: darko.velkov
"""
import zipfile
import shutil

f = open('file.txt','w+')
f.write('One file')
f.close()

f = open('filetwo.txt','w+')
f.write('Two file')
f.close()

comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write('file.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall('extracted_content')

dir_to_zip='/home/user/projects/Python/Python-GH/Complete-Python-3-Bootcamp/12-Advanced Python Modules'
output_filename='example'
shutil.make_archive(output_filename, 'zip', dir_to_zip)
shutil.unpack_archive('example.zip','final_unzip','zip')
