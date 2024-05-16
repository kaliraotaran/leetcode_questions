'''
https://leetcode.com/problems/rotate-list/submissions/1240111386/?envType=study-plan-v2&envId=top-interview-150
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        current = head
        temp = []
        
        while current:
            temp.append(current.val)
            current = current.next
        
        n =  len(temp)
        
        if k >= n:
            k = k % n
            
        if k == 0:
            return head
        
        current = ListNode()
        head = current
        
        for i in range(n - k, n):
            node = ListNode(temp[i])
            current.next = node
            current = current.next
        
        for i in range(n - k):
            node = ListNode(temp[i])
            current.next = node
            current = current.next
        
        return head.next

###########################

        if not head:
            return head
            
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        n = len(arr)   
        if k >=n:
            k = k%n

        
        arr1 = arr[n-k:n]
        arr2 = arr[0:n-k]
        arr3 = arr1+arr2
         

        newhead = None
        for i in arr3:
            if newhead is None:
                newhead = ListNode(i)
                b = newhead
            else:
                b.next = ListNode(i)
                b = b.next
        return newhead
