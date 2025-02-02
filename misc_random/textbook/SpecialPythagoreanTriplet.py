#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 23:03:15 2019

@author: shrikar.amirisetty
"""

import math

for a in range(400):
    abfound = False
    
    for b in range(400):
        if a + b + math.sqrt(a**2 + b**2) == 1000:
            A = a
            B = b
            C = math.sqrt(a**2 + b**2)
            print(int(A*B*C))
            abfound = True
            break
    
    if abfound == True:
        break