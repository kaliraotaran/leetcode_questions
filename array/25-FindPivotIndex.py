'''
https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if sum(nums[i+1:]) == sum(nums[:i]):
                return i
        return -1