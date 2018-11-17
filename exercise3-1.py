#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 18:28:33 2018

@author: andychen
"""

a=int(input("number of days:"))
b=int(input("day of week:"))
weekend=[i for i in range(1,a+1) if ((i+b)%7==0)|((i+b)%7==1)]
print(weekend)