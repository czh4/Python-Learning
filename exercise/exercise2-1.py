#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:13:19 2018

@author: andychen
"""

y=int(input("Year:"))

if y%4==0:
    print(y," is a leap year")
elif y%100==0:
    print(y," is not a leap year")
elif y%400==0:
    print(y," is a leap year")
else:
    print(y," is not a leap year")
