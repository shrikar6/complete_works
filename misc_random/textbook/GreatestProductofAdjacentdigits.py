#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 21:50:56 2019

@author: shrikar.amirisetty
"""

"""
This program finds the largest product of the an input number of adjacent
digits in another input number.
"""

numAnalyze = str(int(input("Input a number: ")))
numTimesMultiply = int(input("Input number of adjacent terms to multiply: "))
largestProduct = 0

for i in range(len(numAnalyze)-numTimesMultiply):
    numAnalyzeSlice = numAnalyze[i:i+numTimesMultiply]
    product = 1

    for x in (range(len(numAnalyzeSlice))):
        product *= int(numAnalyzeSlice[x])
    
    if product > largestProduct:
        largestProduct = product

print(largestProduct)