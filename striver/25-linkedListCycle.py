'''
https://www.naukri.com/code360/problems/cycle-detection-in-a-singly-linked-list_628974?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''

'''
Following is the structure of the Node class already defined.

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
'''

def detectCycle(head) :
    # Write your code here.
    arr = []
    while head:
        if head  in arr:
            return True
        arr.append(head)
        head = head.next
    return False