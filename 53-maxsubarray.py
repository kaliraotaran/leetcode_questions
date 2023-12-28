# https://leetcode.com/problems/maximum-subarray/submissions/1130765660/

class Solution:
    def maxsubarray(self, nums:list[int])->int:
        maxsub = nums[0]
        cursum = 0

        for n in nums:
            if cursum<0:
                cursum=0
            cursum+=n
            maxsub = max(maxsub,cursum)
        return maxsub

maxx = Solution()
print(maxx.maxsubarray([-2, 1,-3, 4, -1, 2, 1, -5, 4]))
