'''
https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1162317982/
here we're given an array and we have to find the sub array with min size that adds upto or is greater than target
initially, we're gonna start iterating through the list and adding the current elements value to total
and then another loop that keeps executing if the total is >= target
then we find the min size window with the formula min(i-left+1) means we subtract the index number of pointer at right(i) 
with the index number of pointer at left and then add one(cause indexing for array starts at 0)
then we also subtract the value that was at the left pointer  from the total.
and then increment left pointer to next value


'''
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left , total = 0,0

        res = float('inf')
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                res= min(i-left +1, res)
                total -=nums[left]
                left+=1
        return 0 if res ==float('inf') else res
    ############ OR ####################
      
        if sum(nums) < target:
            return 0
        s = 0
        l = 0
        ans = len(nums)

        for r, val in enumerate(nums):
            s+= val
            while s>= target:
                s-=nums[l]
                ans = min(ans, r-l+1)
                l+=1
        return ans