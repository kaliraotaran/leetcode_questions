

'''
https://www.codingninjas.com/studio/problems/stack-implementation-using-array_3210209?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''
from sys import *
from collections import *
from math import *
from typing import List

class Stack:
    def __init__(self, n: int):
        # Write your code here
        self.items = []
        self.capacity = n


    def push(self, num: int):
        # Write your code here
        if not self.isFull():
            self.items.append(num)


    def pop(self) -> int:
        # Write your code here
        if not self.isEmpty():
            return self.items.pop()
        else:
            return -1

    def top(self) -> int:
        # Write your code here
        if not self.isEmpty():
            return self.items[-1]
        else:
            return -1

    def isEmpty(self) -> int:
        # Write your code here
        if len(self.items) ==0:
            return 1
        else:
            return 0

    def isFull(self) -> int:
        # Write your code here
        if len(self.items) == self.capacity:
            return 1
        else:
            return 0



