'''
https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

here, the simplest approch would be to pop the elements from the end of the array 
and then insert them to the start of the array


'''

class solution:
    def rotate(self, nums):
        ''' this is done in-place, '''
        i =0 
        n = len(nums)
        k = k%n
        while i<k:
            temp = nums.pop()
            nums.insert(0,temp)
            i+=1
        
        # second approach
        # remove elements k times from end of list and then insert at the 0th index

        for i in range(k):
            a = nums.pop()
            nums.insert(0,a)
            