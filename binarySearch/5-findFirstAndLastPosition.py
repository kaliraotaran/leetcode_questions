

'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/1308628979/?envType=study-plan-v2&envId=binary-search 
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        res =[0,0]
        res[0] = -1
        res[1] = -1

        for i in range(len(nums)):
            if nums[i] ==target:
                res[0] = i
                break
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                res[1] = i
                break
        return res