#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 22:03:10 2025

@author: darko.velkov
"""
import numpy as np
from PIL import Image

mac = Image.open('example.jpg')

type(mac)

mac.crop((0,0,100,100))

penciles = Image.open("pencils.jpg")
penciles.crop((0,0,100,100))

blue = Image.open("blue_color.png")
blue.putalpha(122)
blue.show()