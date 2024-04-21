
'''
https://leetcode.com/problems/linked-list-cycle/submissions/1238191959/?envType=study-plan-v2&envId=top-interview-150
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr = []

        while head:
            if head in arr:
                return True
            arr.append(head)
            head = head.next
        return False
        