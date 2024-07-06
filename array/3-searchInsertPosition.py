
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
        
        #  l =0 
        # r = len(nums)-1
        # mid =0 
        # while l<=r:
        #     mid = (l+r)//2
        #     if nums[mid]<target:
        #         l = mid+1
        #     elif nums[mid]>target:
        #         r = mid-1
        #     else:
        #         return mid
        # return l