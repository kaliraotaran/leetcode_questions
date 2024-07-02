
'''
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/submissions/1306199198/?envType=study-plan-v2&envId=leetcode-75 
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l =0
        r =0 
        k = 1
        for r in range(len(nums)):
            if nums[r] ==0:
                k-=1
            if k <0:
                if nums[l] ==0:
                    k+=1
                l+=1
        return r-l