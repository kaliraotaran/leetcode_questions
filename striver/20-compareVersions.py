'''
https://www.codingninjas.com/studio/problems/compare-versions_1062582?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''

from os import *
from sys import *
from collections import *
from math import *

def compareVersions(a, b):
    #Write your code here
    arr1 = [int(i) for i in a.split('.')]
    arr2 = [int(i) for i in b.split('.')]

    for i in range(max(len(arr1), len(arr2))):
        if i <len(arr1):
            arr3 = arr1[i]
        else:
            arr3 = 0
        
        if i<len(arr2):
            arr4 = arr2[i]
        else:
            arr4 = 0
        
        if arr3>arr4:
            return 1
        if arr3<arr4:
            return -1
    return 0





