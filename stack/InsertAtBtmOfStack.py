'''
https://www.codingninjas.com/studio/problems/insert-an-element-at-its-bottom-in-a-given-stack_1171166?interviewProblemRedirection=true&leftPanelTabValue=SUBMISSION
'''

from os import *
from sys import *
from collections import *
from math import *

def pushAtBottom(myStack: deque, x: int):
	# Write your code here.
	newstack = [x]
	for i in myStack:
		newstack.append(i)
	return newstack