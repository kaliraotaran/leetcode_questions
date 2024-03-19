'''
https://www.codingninjas.com/studio/problems/delete-middle-element-from-stack_985246?interviewProblemRedirection=true&leftPanelTabValue=DISCUSS
'''

from os import *
from sys import *
from collections import *
from math import *

def deleteMiddle(inputStack, N):

    n= len(inputStack)
    del inputStack[((n-1)//2)]
    return inputStack