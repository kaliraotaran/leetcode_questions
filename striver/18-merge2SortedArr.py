'''
https://www.codingninjas.com/studio/problems/ninja-and-sorted-arrays_1214628?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''


from math import *
from collections import *
from sys import *
from os import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    # Write your code here.
    arr1.sort()
    arr2.sort()
    arr1.extend(arr2)
    arr1.sort()
    listt = []
    for i in arr1:
        if i != 0 :
            listt.append(i)
    return listt



