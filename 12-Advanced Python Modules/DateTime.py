#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:55:32 2025

@author: darko.velkov
"""
#import datetime
from datetime import datetime
#mytime=datetime.time(2,10)

#mytime.minute

#print(mytime)

#today = datetime.date.today()
#print(today)

#today.day



mydatetime = datetime(2022,2,1,5,6,3)
mydatetime = mydatetime.replace(year=2025)
print(mydatetime)

from datetime import date

date1 = date(2025,3,3)
date2 = date(2024,3,3)
result = date1-date2
print(result)