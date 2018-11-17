#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 17:39:39 2018

@author: andychen
"""

a=input('String:')
b=a*2

for i in range(len(a)):
    print(b[i:len(b)-i])