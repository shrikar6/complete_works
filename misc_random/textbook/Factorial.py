#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 23:31:57 2018

@author: shrikar.amirisetty
"""

"""
This file calculates the factorial of any given number.
"""

def FirstFactorial(num): 

    num1 = 1
    while num > 0:
        num1 *= num
        num -= 1
    num = num1
    return num

print(FirstFactorial(int(input("Find the factorial of: "))))