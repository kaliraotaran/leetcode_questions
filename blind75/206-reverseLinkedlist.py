# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = []
        while head:
            val.append(head.val)
            head = head.next
        rev = []
        for i in range(len(val)):
            rev.append(val[-i])
        return rev

