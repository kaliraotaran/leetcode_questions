'''
https://leetcode.com/problems/merge-two-sorted-lists/submissions/1203713745/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []

        dummy = list1
        dummy2 = list2
        while dummy:
            arr1.append(dummy.val)
            dummy = dummy.next
        while dummy2:
            arr2.append(dummy2.val)
            dummy2 = dummy2.next
        arr = arr1+arr2
        
        arr.sort()
        newhead = None

        for i in arr:
            if newhead is None:
                newhead = ListNode(i)
                b = newhead
            else:
                b.next = ListNode(i)
                b = b.next
        return newhead