'''

https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/1202831983/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        dummy = head
        while dummy:
            arr.append(dummy.val)
            dummy = dummy.next
        hash1= {}

        for i in arr:
            if i not in hash1:
                hash1[i] = 1
            else:
                if i in hash1:
                    hash1[i] +=1
        arr1 = []
        for keys in hash1.keys():
            arr1.append(keys)
        
        newhead = None
        for i in arr1:
            if newhead is None:
                newhead = ListNode(i)
                b = newhead
            else:
                b.next = ListNode(i)
                b = b.next
        return newhead
    
    ######################## OR ############################
        arr = []
        while head:
            if head.val not in arr:
                arr.append(head.val)
            head = head.next
        newhead = None

        for i in arr:
            if newhead is None:
                newhead = ListNode(i)
                b = newhead
            else:
                b.next = ListNode(i)
                b = b.next
        return newhead