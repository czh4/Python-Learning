#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:14:15 2018

@author: andychen
"""

i=1
list1=[]
while i>0:
    a=int(input("integer:"))
    if a==0:
        break
    else:
        list1.append(a)
        
for j in range(1+len(list1)//2):
    print(list1[j:len(list1)-j:2])
