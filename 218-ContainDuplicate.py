# https://leetcode.com/problems/contains-duplicate/submissions/1133953992/
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        n  = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return True
         
        return False