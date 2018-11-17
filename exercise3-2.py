#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:27:10 2018

@author: andychen
"""

i=1
list1=[]
list2=[]
while i>0:
    a=int(input("integer:"))
    if a==0:
        break
    else:
        list1.append(a)
        
for j in range(len(list1)-1,-1,-1):
    list2.append(list1[j])
    
print(list2)