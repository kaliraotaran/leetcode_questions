'''
https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150

'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        start =0 
        end =0 
        count =0

        for i in range(len(nums)-1):
            start = max(start, i+nums[i])
            if end ==i:
                end = start
                count +=1
        return count

