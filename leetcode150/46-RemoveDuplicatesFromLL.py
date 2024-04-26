

'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/submissions/1242721605/?envType=study-plan-v2&envId=top-interview-150
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        hash = {}
        for i in arr:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i]+=1
        new = []
        for key, value in hash.items():
            if value ==1:
                new.append(key)
        newhead = None
        for i in new:
            if newhead is None:
                newhead = ListNode(i)
                b = newhead
            else:
                b.next = ListNode(i)
                b = b.next
        return newhead