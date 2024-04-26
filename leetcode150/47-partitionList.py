
'''
https://leetcode.com/problems/partition-list/submissions/1242726529/?envType=study-plan-v2&envId=top-interview-150
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        s = []
        l = []
        for i in arr:
            if i < x:
                s.append(i)
            else:
                l.append(i)
        a= s+l
        if a == []:
             return 
        newhead = None
        for i in a:
            if newhead is None:
                newhead = ListNode(i)
                b = newhead
            else:
                b.next = ListNode(i)
                b = b.next
        return newhead