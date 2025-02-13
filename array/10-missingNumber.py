

'''
https://leetcode.com/problems/missing-number/ 
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        # summ = sum(nums)
        # c = 0
        # for i in range( len(nums)+1):
        #     c+=i
        # return c - summ

        # ORR
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)