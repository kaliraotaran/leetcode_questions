# https://leetcode.com/problems/maximum-subarray/submissions/1162288995/
'''
we initially have an array
we move from left to right and initialize 2 variables cursum and maxsub
then, while looping the array, we add the current element to the cursum, 
if the sum(value) of cursum becomes -ve we reset it(that just means that we sorta skip or 
ignore teh previous values that we've visited  so far because they added up to a negative number
and would in the end effect the sum of our subarray).
and then we find the maximum between the cursum and the previous maximum
and then in the end we return the maximum  value as the result.

'''

class Solution:
    def maxsub(self, nums:list[int]):
        maxsub  = nums[0]
        cursum = 0

        for i in nums:
            if cursum < 0:
                cursum  =0 
            cursum += i
            maxsub = max(cursum, maxsub)
        return maxsub
    
