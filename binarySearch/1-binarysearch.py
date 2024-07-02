
'''
https://leetcode.com/problems/binary-search/?envType=study-plan-v2&envId=binary-search 
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l =0 
        h = len(nums)-1
        m =0

        while l<=h:
            mid = (l+h)//2
            if nums[mid] ==target:
                return mid
            elif nums[mid]>target:
                h = mid-1
            else:
                l = mid+1
        return -1