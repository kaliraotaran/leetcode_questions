'''
https://leetcode.com/problems/reverse-linked-list/

in this method, the main objective is to take the values from the linkedlist and 
put it into an array for furthur operations
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeList = []
        while head:
            nodeList.append(head)
            head = head.next

        leng = len(nodeList)
        for i in range(leng-1, 0, -1):
            nodeList[i].next = nodeList[i-1]
        if nodeList:
            nodeList[0].next = None
            return nodeList[-1]
        return None
