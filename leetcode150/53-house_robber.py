

'''
https://leetcode.com/problems/house-robber/submissions/1256732206/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        even = nums[0]
        odd = nums[1]

        for i in range(2, len(nums)):
            if (i%2==0):
                odd = max(even , odd)
                even += nums[i]
            else:
                even = max(even , odd)
                odd += nums[i]
        return max(even , odd)

        