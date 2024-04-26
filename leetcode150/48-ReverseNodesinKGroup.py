
'''
https://leetcode.com/problems/reverse-nodes-in-k-group/?envType=study-plan-v2&envId=top-interview-150
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], g: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        k = []
        for i in range(0,len(arr),g):   
            temp = arr[i:i+g]
            if len(temp) == g:
                k+=temp[::-1]
            else:
                k+=temp
        
        newhead = None
        for i in k:
            if newhead is None:
                newhead = ListNode(i)
                b = newhead
            else:
                b.next = ListNode(i)
                b = b.next
        return newhead