

'''
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next    
        l =0
        r = len(arr)-1  
        m = 0
        while l<r:
            s = arr[l]+arr[r]
            m = max(m, s)
            l+=1
            r-=1
        return m