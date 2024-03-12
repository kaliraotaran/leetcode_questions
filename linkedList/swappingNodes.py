

'''
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/submissions/1201810607/


'''


class ListNode:
    def __init__(self, val =0 , next = None):
        self.val = val
        self.next = next
class Sol:
    def swap(self, head:ListNode, k):
        # here, we're gonna take the values from the LL and put it into the array
        arr = []
        dummy = head # make sure to operate on head using a variable, not the head directly
        while dummy:
            arr.append(dummy.val)
            dummy = dummy.next

        # here, we're actually swapping the values at the Kth postion from the back and front
        n = len(arr)
        left, right = k-1, n-k
        arr[left],arr[right] = arr[right], arr[left]

        # here, we're gonna convert the array into a LL 
        dummy = head
        i =0 
        while dummy:
            dummy.val = arr[i]
            i+=1
            dummy = dummy.next
        return head