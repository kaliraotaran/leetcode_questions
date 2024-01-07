# https://leetcode.com/problems/merge-two-sorted-lists/submissions/1138729229/

class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None
    
class Solution(object):
    def merge(self, l1, l2):
        dummy = ListNode() 
        tail = dummy

        while l1 and l2:  # going top use a form of linked list
            if l1.val <= l2.val:  
                tail.next = l1 # adding the value of l1 to the end of the dummy list
                l1 = l1.next # moving onto the next value in l1
            else:
                tail.next = l2.val # adding value of l2 to the end of the list
                l2 = l2.next   # moving pointer to next value in l2
            tail= tail.next # moving the pointer to the next value in the dummy list
        if l1 or l2: # if l1 or l2 are null or empty and just one list exists
            tail.next = l1 or l2
        return dummy.next 

sol = Solution()
print(sol.merge([1,2,4],[1,3,5]))