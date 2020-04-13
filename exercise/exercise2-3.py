#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:44:09 2018

@author: andychen
"""

n=int(input("Integer:"))
a=0
b=1
for i in range(n):
    if i==0:
        print(a,end=" ")
    else:
        print(b,end=" ")
        c=a
        a=b
        b+=c

    
