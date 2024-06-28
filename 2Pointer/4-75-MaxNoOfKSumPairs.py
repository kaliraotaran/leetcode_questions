
'''
https://leetcode.com/problems/max-number-of-k-sum-pairs/submissions/1302853799/?envType=study-plan-v2&envId=leetcode-75
'''


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        count =0 
        while l<r:
            summ = nums[l]+nums[r]

            if summ  == k:
                count+=1
                l+=1
                r-=1
            
            elif summ > k:
                r-=1
            else:
                l+=1

        return count