#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:19:10 2019

@author: shrikar.amirisetty
"""

"""
MaleNames = open("MaleNamesFile.txt", "r")
NewMaleNames = open("MaleNamesFileNew.txt", "w+")

MaleNameslines = MaleNames.readlines()

for i in MaleNameslines:
    line = i[8:len(i)]
    lenName = 0
    for x in line:
        if x == "<":
            Name = line[0:lenName]
            break
        else:
            lenName += 1
    NewMaleNames.write(Name + " ")

MaleNames.close()
NewMaleNames.close()

FemaleNames = open("FemaleNamesFile.txt", "r")
NewFemaleNames = open("FemaleNamesFileNew.txt", "w+")

FemaleNameslines = FemaleNames.readlines()

for i in FemaleNameslines:
    line = i[8:len(i)]
    lenName = 0
    for x in line:
        if x == "<":
            Name = line[0:lenName]
            break
        else:
            lenName += 1
    NewFemaleNames.write(Name + " ")

FemaleNames.close()
NewFemaleNames.close()
"""

name = str(input("Input a name: ")).upper()
gender = str(input("Input a gender (only the letter): ")).upper()

if gender == "M":
    PossibleNames = open("MaleNamesFileNew.txt", "r")
elif gender == "F":
    PossibleNames = open("FemaleNamesFileNew.txt", "r")

PossibleNamesList = PossibleNames.read()
PossibleNamesList = PossibleNamesList.split()

BestNameReplacement = [0, ""]

for i in PossibleNamesList:
    compatability = 0
    if len(name) <= len(i):
        for x in range(len(name)):
            if name[x] == i[x]:
                compatability += 1
    else:
        for x in range(len(i)):
            if name[x] == i[x]:
                compatability += 1
    if name[0] == i[0]:
        compatability += 2
    if len(name) == len(i):
        compatability += 1
    if compatability > BestNameReplacement[0]:
        BestNameReplacement = [compatability, i]
    elif compatability == BestNameReplacement[0]:
        BestNameReplacement += [i]

print("Best possible name replacements are the following: ")
for i in range(len(BestNameReplacement) - 1):
    print(BestNameReplacement[i+1])