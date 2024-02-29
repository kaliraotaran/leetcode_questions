# https://leetcode.com/problems/binary-search/description/

class Solution:
    def binary(self, nums:list, target):
        if target in nums:
            return nums.index(target)
        else:
            return -1
sol = Solution()
print(sol.binary([1,4,9,14], 4))