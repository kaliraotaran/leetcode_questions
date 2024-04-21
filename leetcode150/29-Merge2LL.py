'''
https://leetcode.com/problems/merge-two-sorted-lists/submissions/1238195197/?envType=study-plan-v2&envId=top-interview-150
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []

        arr2= []
    
        dumm1 = list1
        dumm2 = list2
        while dumm1:
            arr1.append(dumm1.val)
            dumm1 = dumm1.next
        while dumm2:
            arr2.append(dumm2.val)
            dumm2 = dumm2.next

        arr = arr1+arr2
        arr.sort()
        newhead = None

        for i in arr:
            if newhead is None:
                newhead= ListNode(i)
                b = newhead
            else:
                b.next = ListNode(i)
                b = b.next
        return newhead