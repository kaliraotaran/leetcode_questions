

'''
https://www.codingninjas.com/studio/problems/intersection-of-linked-list_630457?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findIntersection(firstHead, secondHead):
    a = firstHead
    b= secondHead

    while a != b:
        a = secondHead if a is None else a.next
        b = firstHead if b is None else b.next

    return a

