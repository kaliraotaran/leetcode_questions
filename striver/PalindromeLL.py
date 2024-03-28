'''
https://www.naukri.com/code360/problems/palindrom-linked-list_799352?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''


from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

#Following is the class structure of the LinkedListNode class:
class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None
            
            
def isPalindrome(head):
    
    # Write your code here.
    arr = []
    while head:
        arr.append(head.data)
        head= head.next
    left = 0
    right = len(arr)-1
    while left<right:
        if arr[left] == arr[right]:
            left+=1
            right -=1
        else:
            return False
    return True
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    
    
def takeinput():
    
    inputlist=[int(ele) for ele in input().split()]
    
    head=None
    tail=None
    
    for currentData in inputlist:
        
        if currentData == -1:
            break
        
        Newnode=Node(currentData)
        
        if head is None:
            head=Newnode
            tail=Newnode
        else:
            tail.next=Newnode
            tail=Newnode
            
    return head







#Main
t = int(stdin.readline().rstrip())

while t > 0:
    
    head = takeinput()
    
    if isPalindrome(head):
        print('true')
    else:
        print('false')
        
    t -= 1
