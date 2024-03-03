'''
https://www.codingninjas.com/studio/problems/maximum-subarray-sum_630526?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
    maxsum = arr[0]
    cursum = 0 

    for i in arr:
        if cursum<0:
            cursum =0 
        cursum+=i
        maxsum = max(cursum, maxsum)
    if maxsum <0:
        maxsum =0 
    return maxsum






def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
