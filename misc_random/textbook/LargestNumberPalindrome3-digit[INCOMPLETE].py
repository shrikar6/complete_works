#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 18:48:50 2019

@author: shrikar.amirisetty
"""

import math

def largestPalindrome():
    x = 997
    while x > 100:
        product = str(x)
        palindrome = product
        
        while product != "":
            palindrome += product[len(product)-1]
            product = product[0:len(product)-1]
            
        palindrome = int(palindrome)
        listFactors = []    
        
        for i in range(palindrome):
            if i+1 > math.sqrt(palindrome):
                break
            if palindrome%(i+1) == 0 and i != 0:
                if len(str(i+1)) == 3 and len(str(palindrome/(i+1))) == 3:
                    return(palindrome)
                listFactors += [(i+1, int(palindrome/(i+1)))]
        x -= 1
