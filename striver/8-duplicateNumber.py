'''
https://www.codingninjas.com/studio/problems/find-duplicate-in-array_1112602?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''


from sys import *
from collections import *
from math import *

def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    hash1 = {}
    for i in arr:
        if i not in hash1:
            hash1[i] = 1
        else:
            if i in hash1:
                hash1[i] +=1
    for keys, values in hash1.items():
        if values>1:
            return keys