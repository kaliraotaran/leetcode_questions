
'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1202826745/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        dummy= head
        while dummy:
            arr.append(dummy.val)
            dummy = dummy.next
        arr.pop(-n)
        
        
        newhead = None
        
        for i in arr:
            if newhead is None:
                newhead = ListNode(i)
                b = newhead
            else:
                b.next = ListNode(i)
                b = b.next
        return newhead