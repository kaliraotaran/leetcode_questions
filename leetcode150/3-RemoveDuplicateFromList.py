'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

it is moving through the list and it removes duplicate element at the left of the list
and it only executes the if statement if the element at the left is not the same as the 
element at the right of the list
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for i in range(1, len(nums)):
            if nums[left] != nums[i]:
                left+=1
                nums[left] = nums[i]
        return left+1
