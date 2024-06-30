'''
https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75 
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        cursum =msub = sum(nums[:k])

        for i in range(k,len(nums)):  
            cursum += nums[i] - nums[i-k]    
            msub = max(msub, cursum)
        
        return msub/k