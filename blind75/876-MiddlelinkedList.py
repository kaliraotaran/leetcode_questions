# https://leetcode.com/problems/middle-of-the-linked-list/

'''
here we're gonna use the 2 pointer method with a slow pointer and a fast pointer
the fast pointer does 2 iteration for every one iteration of the slow pointer
whem the fast pointer reaches the end of the linked list, it means its reached last node 
        or is now out of bounds
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) :
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    '''by the time fast gets to the end, low gets to teh middle of the list'''