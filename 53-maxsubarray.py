# https://leetcode.com/problems/maximum-subarray/submissions/1130765660/
'''
we take 2 varaibles maxsubarray and a cursum, and then we iterate through the list
we add the current number with the value of cursum
if value of cursum is greater than maxsubarray(which is initally set to the first number in teh list)
then we update maxsubarray with value of cursum 
if the value of cursum becomes <=0, we update value of cursum back to 0

'''
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
