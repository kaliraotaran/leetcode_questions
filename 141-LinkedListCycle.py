# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# we use 2 pointer and move them through the list, if the slow pointer later catches up 
        # with the fast one then there is a cycle in the linked list
class Solution:
    def hasCycle(self, head:[ListNode])->bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False