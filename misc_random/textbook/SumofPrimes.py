#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:39:09 2019

@author: shrikar.amirisetty
"""

maxNum = int(input("Input a number: "))
sumPrimes = 0
currentNum = 2

while currentNum != maxNum:
    isPrime = True
    
    for i in range(currentNum):
        if i == 0 or i == 1:
            pass
        elif currentNum%i == 0:
            isPrime = False
            break
    
    if isPrime == True:
        sumPrimes += currentNum
    currentNum += 1

print(sumPrimes)