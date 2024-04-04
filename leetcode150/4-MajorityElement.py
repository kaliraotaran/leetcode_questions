'''
https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]