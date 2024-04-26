

'''
https://leetcode.com/problems/reverse-linked-list-ii/submissions/1242717406/?envType=study-plan-v2&envId=top-interview-150
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        left-=1
        right-=1
        while left<=right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right]= temp
            left+=1
            right-=1
        newhead = None
        for i in arr:
            if newhead is None:
                newhead = ListNode(i)
                b = newhead
            else:
                b.next = ListNode(i)
                b = b.next
        return newhead