# https://leetcode.com/problems/linked-list-cycle/description/

'''
this is a simple slow and fast pointer problem 
slow pointer moves one step at a time, while the fast pointer moves two 
steps at a time.
if the fast pointer catches up to the slow pointer that means there is 
a cycle in the list

we use slow and fast pointer and set them both to the head of the list
and we keep looping until the current and the next to current node exits(for the fast)
we then iterate the slow pointer by one and the fast by 2
when they meet it means there is a loop
else we return false


'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def loop(self, head:ListNode):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False