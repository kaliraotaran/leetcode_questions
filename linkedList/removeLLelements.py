'''
https://leetcode.com/problems/remove-linked-list-elements/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        arr = []
        dummy = head

        while dummy:
            if dummy.val != val:
                arr.append(dummy.val)
            dummy = dummy.next

        
        newhead = ListNode(0,None)
        dummy = newhead
        for i in range(len(arr)):
            dummy.next = ListNode(arr[i], None)
             
            dummy= dummy.next
        return newhead.next