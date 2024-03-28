'''
https://www.naukri.com/code360/problems/reverse-the-singly-linked-list_799897?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''

from math import *
from collections import *
from sys import *
from os import *

"""***************************************************************

    Following is the class structure of the LinkedListNode class:




*****************************************************************"""
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

def reverseLinkedList(head):
    # Write your code here.

    prev = None
    current = head
    while(current!= None):
        nextnode = current.next
        current.next = prev
        prev = current
        current = nextnode
    return prev
   










