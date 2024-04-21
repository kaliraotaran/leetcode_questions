'''
https://leetcode.com/problems/add-two-numbers/submissions/1238417023/?envType=study-plan-v2&envId=top-interview-150
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        dumm = l1
        while dumm :
            arr1.append(dumm.val)
            dumm = dumm.next

        arr2 = []
        dumm2 = l2
        while dumm2:
            arr2.append(dumm2.val)
            dumm2 = dumm2.next
       
        num1 = ''
        num2 = ''
        for i in reversed(range(len(arr1))):
            num1+=str(arr1[i])
        for i in reversed(range(len(arr2))):
            num2+=str(arr2[i])
        summ =0
        summ = str(int(num1)+int(num2))
        arr3= [int(summ[i]) for i in reversed(range(len(summ)))]

        newhead = None

        for i in arr3:
            if newhead is None:
                newhead = ListNode(i)
                b = newhead
            else:
                b.next = ListNode(i)
                b = b.next
        return newhead

                