

'''
https://leetcode.com/problems/middle-of-the-linked-list/submissions/1203743981/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head)
            head = head.next
        
        mid = len(arr)//2
        return arr[mid]

