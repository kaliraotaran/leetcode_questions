
''' 
https://leetcode.com/problems/climbing-stairs/submissions/1238080335/?envType=study-plan-v2&envId=top-interview-150

'''

class Solution:
    def climbStairs(self, n: int) -> int:
        lis = [1,1]
        num =0 
        for i in range(n-1):
            lis.append(lis[-1]+lis[-2])
        return lis[-1]