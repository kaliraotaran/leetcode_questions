

'''
https://leetcode.com/problems/search-insert-position/submissions/1243474361/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       

        for i in range(len (nums)):
            if nums[i] > target or nums[i] == target:
                return i
        return len(nums)