#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 16:05:03 2019

@author: shrikar.amirisetty
"""

"""
This program finds the difference between the sum of the squares and the square
of the sum of numbers between 1 and any input number.
"""

maxNum = int(input("Input a number: "))
sumofSquares = 0
squareofSum = 0

for i in range(maxNum):
    sumofSquares += (i+1)**2
    squareofSum += i+1

squareofSum **= 2
print(squareofSum - sumofSquares)