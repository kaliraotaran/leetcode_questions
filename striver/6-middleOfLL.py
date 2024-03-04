
'''
https://www.codingninjas.com/studio/problems/middle-of-linked-list_973250?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=DISCUSS
'''


from math import *
from collections import *
from sys import *
from os import *

'''

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''

def findMiddle(head):
    # Write your code here
    # head denoted head of linked list
    newnode = head
    midnode = head

    length = 0
    i =1

    while newnode is not None:
        # here we're gonna get the length of the linked list by iterating through 
            # each and every element and keeping count
        length +=1
        newnode = newnode.next

    if length %2 !=0:  # for lists with odd length
        mid = (length+1)/2
        while i <mid:     # this loop will go till it reaches middle
            midnode = midnode.next
            i+=1
        return midnode
    else:
        mid = (length +2)/2 # for lists of even length 
        while i <mid:
            midnode = midnode.next
            i+=1
        return midnode


