# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

'''
this is sortof a 2 pointer question ,
we first have a left pointer set to 0
and then we start iterating the list from the 2 element(so it would be the 1th element)
if the element at left is not equal to element at the ith position ,
we then set the value at left poition to value at ith position
and then increment left pointer
in the end we print the length of left pointer  which represents the number of non duplicate elements in the array +1

'''
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # this solution didnt work in leetcode, but it bascailly created a new list and removed duplicates when i set it to a set
        # newlist = set(nums)
        # return len(newlist)
        left = 0
         
        for i in range(1,len(nums)):
            if nums[left] != nums[i]:
                left+=1
                nums[left] = nums[i]
        return left+1

sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))