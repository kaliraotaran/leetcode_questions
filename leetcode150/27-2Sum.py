'''
https://leetcode.com/problems/two-sum/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i]+nums[j]==target:
                    return [i, j]
 
    
