#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 16:19:30 2019

@author: shrikar.amirisetty
"""

"""
This program prints the nth prime number starting from 2, where n is input by the user.
"""

whichPrime = int(input("Input a number: "))
listPrimes = []
numPrime = 2

while len(listPrimes) != whichPrime:
    isPrime = True
    
    for i in range(numPrime):
        if i == 0 or i == 1:
            pass
        elif numPrime%i == 0:
            isPrime = False
            break
    
    if isPrime == True:
        listPrimes += [numPrime]
    numPrime += 1

print(listPrimes[whichPrime - 1])
