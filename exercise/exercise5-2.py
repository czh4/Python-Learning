#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 17:45:49 2018

@author: andychen
"""

a=input('String:')

for i in range(len(a)):
    print(a[0:i+1],end='')
for j in range(len(a)):
    print(a[j+1:len(a)+1],end='')
