

'''
https://leetcode.com/problems/longest-consecutive-sequence/
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0 :
            return 0
        nums.sort()
        maxi = 1
        curmax = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1]+1:
                curmax +=1
            else:
                curmax = 1
            maxi = max(maxi ,curmax)
        return maxi


