#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:28:48 2018

@author: andychen
"""

a=int(input("integer:"))
while a>9:
    b=a%10
    print(b)
    a=a//10
print(a)
