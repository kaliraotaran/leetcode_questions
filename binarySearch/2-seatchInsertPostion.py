
'''
https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=binary-search 
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l =0 
        r = len(nums)-1
        mid =0 
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
            else:
                return mid
        return l