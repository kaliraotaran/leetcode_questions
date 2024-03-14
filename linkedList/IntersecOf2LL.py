'''
https://leetcode.com/problems/intersection-of-two-linked-lists/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        arr1 = []
         
        arr2 =[]
        while headA or headB:
            if headA:
                if headA in arr2:
                    return headA
                arr1.append(headA)
                headA = headA.next
            
            if headB:
                if headB in arr1:
                    return headB
                arr2.append(headB)
                headB = headB.next
            