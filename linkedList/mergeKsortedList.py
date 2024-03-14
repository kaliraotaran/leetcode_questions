'''
https://leetcode.com/problems/merge-k-sorted-lists/submissions/1203719407/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []

        for i in range(len(lists)):
            while lists[i]:
                arr.append(lists[i].val)
                lists[i] = lists[i].next
        arr.sort()
        newhead = None
        for i in arr:
            if newhead is None:
                newhead = ListNode(i)
                b = newhead
            else:
                b.next = ListNode(i)
                b= b.next
        return newhead