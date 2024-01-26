# https://leetcode.com/problems/contains-duplicate/submissions/1133953992/
'''
firstly, we'll sort the list
if the len of hte list is 1, there's no way that there're duplicate nums
we then start eh loop from teh second element in the list and compare it with the prev element
if they are the same, means there's a duplicate
   ( you can also just normally iterate the list from beg to end and compare with the +1 element)
'''



class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        n  = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return True
         
        return False