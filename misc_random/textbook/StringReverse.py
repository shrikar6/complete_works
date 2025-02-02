#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 23:28:13 2018

@author: shrikar.amirisetty
"""

"""
This piece of code reverses any given string.
"""

def FirstReverse(str): 

    str1 = ""
    while str != "":
        str1 += str[-1]
        str = str[0:-1]
    str = str1
    return str
     
print(FirstReverse(str(input("Reverse a string: "))))