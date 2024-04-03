'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for i in range(1, len(nums)):
            if nums[left] != nums[i]:
                left+=1
                nums[left] = nums[i]
        return left+1
