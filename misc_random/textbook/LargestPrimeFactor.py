#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 17:33:27 2018

@author: shrikar.amirisetty
"""

"""
This program lists the prime factors of any given number
"""

import math

number = int(input("Input number: "))
listFactors = []
listPrimeFactors = []

for i in range(number):
    if i+1 > math.sqrt(number):
        break
    if number%(i+1) == 0 and i != 0:
        listFactors += [i+1, int(number/(i+1))]

for i in listFactors:
    Prime = True
    for x in range(i):
        if i%(x+1) == 0 and x != 0 and x != i-1:
            Prime = False
            break
    if Prime == True:
        listPrimeFactors += [i]

print(max(listPrimeFactors))