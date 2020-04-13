#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 17:20:05 2018

@author: andychen
"""

t=float(input('Time period in seconds:'))
h=t//3600
m=(t%3600)//60
s=(t%3600)%60
print(h,'h',m,'m',s,'s')
