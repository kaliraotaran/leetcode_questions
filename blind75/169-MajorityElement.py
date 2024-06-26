# https://leetcode.com/problems/majority-element/submissions/1149724153/
'''
we simply jsut sort the list and then we return teh element in the middle 
by applying floor division of the number of elements by 2

'''

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # themap = {}
        # res, maxmap =0,0
        # for n in nums:
        #     themap[n] = 1 +themap.get(n,0)
        #     res = n if themap[n] > maxmap else res
        #     maxmap = max(themap[n], maxmap)
        # return res
        '''the second approach'''
        nums.sort()
        n = len(nums)
        # return nums[n//2]
        return nums[(len(nums)//2)]
        '''
        [2,3,2,3,3]
        [2,2,3,3,3] - teh sorted list
        len = 5
        n//2 -- 5//2 - 2
        nums[2] - returns 3 

        '''
sol = Solution()
print(sol.majorityElement([1,1,2,2,2]))
 