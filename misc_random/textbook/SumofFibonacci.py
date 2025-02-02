#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 17:16:14 2018

@author: shrikar.amirisetty
"""

"""
This program takes a number and adds all multiples of that number that are part
of the Fibonacci sequence, under a maximum threshold.
"""

fibonacciSum = 0
fibonacciOld = 1
fibonacciNew = 1
MaxExtent = int(input("Input maximum value before termination: "))
Multiple = int(input("Input factor: "))

while fibonacciNew <= MaxExtent:
    fibonacciTransit = fibonacciOld + fibonacciNew
    fibonacciOld = fibonacciNew
    fibonacciNew = fibonacciTransit
    if fibonacciOld%Multiple == 0:
        fibonacciSum += fibonacciOld

print(fibonacciSum)
