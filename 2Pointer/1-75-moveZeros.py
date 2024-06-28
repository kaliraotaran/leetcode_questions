'''
https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if len(nums)==2:
        #     if nums[0] == 0:
        #         nums[0], nums[1] = nums[1], nums[0]
        # l  =0 
        # r  = 1
        # while r<len(nums)-1:
        #     if nums[l] ==0  and nums[r] !=0:
        #         nums[l], nums[r] = nums[r] , nums[l]
        #     if nums[l] ==0 and nums[r]==0:
        #         nums[r], nums[r+1] = nums[r+1], nums[r]
        #         nums[l], nums[l+1] = nums[l+1], nums[l]
        #     if nums[r] ==0  and nums[l] !=0:
        #         nums[r], nums[r+1] = nums[r+1] , nums[r]
        #     l +=1
        #     r+=1
        # return nums
        left =0 
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
        