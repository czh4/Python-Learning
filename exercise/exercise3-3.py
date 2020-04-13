#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:54:28 2018

@author: andychen
"""

a=int(input("a:"))
b=int(input("b:"))
if b!=0:
    b,a=a%b,b
print(a)
