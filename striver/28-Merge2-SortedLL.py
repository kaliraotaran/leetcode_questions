'''
https://www.naukri.com/code360/problems/merge-two-sorted-linked-lists_800332?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''

'''
    Following is the linked list node structure:'''
class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

def sortTwoLists(first, second):
    arr1 = []
    arr2 = []
    dummy1 = first
    while dummy1:
        arr1.append(dummy1.data)
        dummy1 = dummy1.next
    dummy2 = second
    while dummy2:
        arr2.append(dummy2.data)
        dummy2 = dummy2.next
 
    arr = arr1 +arr2
    arr.sort()
    newhead = None
    for i in arr:
        if newhead is None:
            newhead = Node(i)
            b = newhead
        else:
            b.next = Node(i)
            b =b.next
    return newhead