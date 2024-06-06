
'''
https://leetcode.com/problems/search-insert-position/
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        

        for i in range(len(nums)):
            if nums[i]>target or nums[i] == target:
                return i
        return len(nums) # this means that the element belongs at the end since its the largest
                            # because it did not belong in the for loop above(wasn't in the array)