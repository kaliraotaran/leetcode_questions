
'''
https://leetcode.com/problems/reverse-linked-list/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        newhead = self.reverseList(head.next)
        front = head.next
        front.next = head

        head.next = None

        return newhead
