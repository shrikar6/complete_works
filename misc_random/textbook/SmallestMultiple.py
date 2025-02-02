#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 15:06:20 2019

@author: shrikar.amirisetty
"""

"""
This file calculates the smallest multiple of all numbers between 1 and any input number
"""

maxNumRange = int(input("Input a number: "))
smallestMultiple = 1
multipliedNumbers = [1]

for num in range(maxNumRange):
    num3 = num
    
    for num2 in multipliedNumbers:
        if num3 == 0:
            pass
        elif num3%num2 == 0:
            num3 /= num2
    
    if num3 != 1 and num3 != 0:
        smallestMultiple *= num3
        multipliedNumbers += [int(num3)]

print(int(smallestMultiple))