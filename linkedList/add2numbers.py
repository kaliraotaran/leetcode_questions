'''
https://leetcode.com/problems/add-two-numbers/submissions/1202843237/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        arr1 , arr2 = [],[]

        while l1:
            arr1.append(l1.val)
            l1= l1.next
        while l2:
            arr2.append(l2.val)
            l2 = l2.next
        
        num1 = ''
        num2= ''
        for i in reversed(range(len(arr1))):
            num1+= str(arr1[i])
        for i in reversed(range(len(arr2))):
            num2 += str(arr2[i])
        arr3 = str(int(num1) +int(num2))
        finalarray = [int(arr3[i]) for i in reversed(range(len(arr3)))]

        newhead = None
        for i in finalarray:
            if newhead is None:
                newhead = ListNode(i)
                b = newhead
            else:
                b.next = ListNode(i)
                b = b.next
        return newhead