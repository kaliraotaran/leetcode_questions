
'''
https://leetcode.com/problems/jump-game/submissions/1283113799/
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        jumps = nums[0]

        for i in nums:
            if jumps<0:
                return False
            elif i > jumps:
                jumps = i
            jumps-=1
        return True
        

