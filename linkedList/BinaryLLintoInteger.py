
'''
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/1201822008/
'''

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None
    
class Sol:
    def Binary(self, head:ListNode):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        sol = 0
        n = len(arr)
        for i in range(n):
            sol+= arr[i] *pow(2,n-i-1)
        return sol