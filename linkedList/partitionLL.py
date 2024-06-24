'''
https://leetcode.com/problems/partition-list/'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# class Solution:
#     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # arr = []
        # while head:
        #     arr.append(head.val)
        #     head = head.next
        # smaller = []
        # larger = []
        # for i in arr:
        #     if i <x:
        #         smaller.append(i)
        #     else:
        #         larger.append(i)
        # answer = smaller+larger
        # if answer == []:
        #     return 
        # head = temp = ListNode(answer[0])
        # for i in range(1, len(answer)):
        #     temp.next = ListNode(answer[i])
        #     temp = temp.next
        # return head




class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head =head.next
        s = []
        l = []
        for i in arr:   
            if i <x:
                s.append(i)
            else:
                l.append(i)
        a = s+l
        newhead = None
        for i in a:
            if newhead is None:
                newhead = ListNode(i)
                b = newhead
            else:
                b.next = ListNode(i)
                b = b.next
        return newhead
