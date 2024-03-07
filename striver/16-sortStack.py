

'''
https://www.codingninjas.com/studio/problems/sort-a-stack_985275?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION

'''


from os import *
from sys import *
from collections import *
from math import *

def sort_substack(stack,n):
    # base case 
    if not stack:
        stack.append(n)
        return 
    if stack[-1] < n:
        stack.append(n)
        return 
    x = stack.pop()
    sort_substack(stack, n)
    stack.append(x)

def sortStack(stack):
    
     # base case 
    if not stack:
        return 
    n = stack.pop()
    sortStack(stack)

    sort_substack(stack, n)