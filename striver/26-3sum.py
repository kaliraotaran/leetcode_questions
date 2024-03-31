
'''
https://www.naukri.com/code360/problems/triplets-with-given-sum_893028?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''


from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit

def findTriplets(arr, n, k):
    
    # Write your code here.
    ans = list()
    arr = sorted(arr)

    i =0
    while i<n:
        target = k - arr[i]  
        left = i+1
        right = n-1
        while left<right :
            summ = arr[left]+arr[right]
            if summ<target:
                left+=1
            elif summ>target:
                right -=1
            else:
                x, y = arr[left], arr[right]
                ans.append([arr[i], x, y])
                while left <right and arr[left] == x:
                    left+=1
                while left <right and arr[right]==y:
                    right -=1
        while i +1 <n and arr[i] == arr[i+1]:
            i+=1
        i+=1
    return ans


















# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    K = int(stdin.readline())
    return N, arr,K


tc = int(input())
while tc > 0:
    N, arr,K = takeInput()
    ans = findTriplets(arr, N,K)

    if len(ans) == 0:
        stdout.write("-1\n")

    else:
        for i in ans:
            i.sort()
            stdout.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

    tc -= 1
