
'''
https://leetcode.com/problems/odd-even-linked-list/?envType=study-plan-v2&envId=leetcode-75
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        x = [arr[i] for i in range(len(arr)) if i %2==0]
        y = [arr[i] for i in range(len(arr)) if i %2 ==1]
        arr = x+y
        newhead = None

        for i in arr:
            if newhead is None:
                newhead = ListNode(i)
                b =newhead
            else:
                b.next = ListNode(i)
                b =b.next
        return newhead
