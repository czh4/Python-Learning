#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:00:25 2018

@author: andychen
"""

n=int(input("Integer:"))
for i in range(1,n+1):
    s=0
    for j in range(1,i):
        if i%j==0:
            s+=1
    if s==1:
        print(i,end=" ")
