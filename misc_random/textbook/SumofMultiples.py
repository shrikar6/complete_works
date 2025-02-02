#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 22:52:21 2018

@author: shrikar.amirisetty
"""

"""
This program is designed to find the sum of the multiples of 2 numbers input by the user,
under a threshold maximum number, which is also input by the user.
"""

x = 0
multiples1 = int(input("Insert a number: "))
multiples2 = int(input("Insert another number: "))
xMax = int(input("Calculate sum of all multiples of " + str(multiples1) + " and " + str(multiples2) + " below: "))
sumofmultiples = 0

while x < xMax:
    if x%multiples1 == 0 or x%multiples2 == 0:
        sumofmultiples += x
    x += 1

print(sumofmultiples)