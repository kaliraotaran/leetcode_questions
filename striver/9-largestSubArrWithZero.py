

'''
https://www.codingninjas.com/studio/problems/longest-subset-zero-sum_920321?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''

from math import *
from collections import *
from sys import *
from os import *

def LongestSubsetWithZeroSum(arr):

    # Write your Code here.
    # Return an integer denoting the answer.
    maxx = 0

    for i in range(len(arr)):

        cursum =0 
        for j in range(i, len(arr)):
            cursum +=arr[j]
            if cursum ==0:
                maxx = max(maxx, j-i+1)
    return maxx


