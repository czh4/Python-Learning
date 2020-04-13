#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 19:52:41 2018

@author: andychen
"""

n=int(input("Number of Rows:"))

'''
Generating seperator
'''

p='+'
m='-'
sep1=p+m*n+p+m*8+p

'''
Part A
'''

x='n'
y='pi'
print(sep1)
print(f'|{x:^{n}}|{y:^8}|')
print(sep1)

'''
Part B
'''

for i in range(n):
    z=10**i
    pi=0
    for j in range(z):
        pi += (-1) ** j * 4 / (2 * j + 1)
    print(f'|{z:>{n}}|{pi:.6f}|')

'''
Part C
'''

print(sep1)
