'''
https://leetcode.com/problems/sqrtx/?envType=study-plan-v2&envId=top-interview-150
'''

 
class Solution:
    def mySqrt(self, x: int) -> int:

        if x <=2:
            return x
        
        i = 2
        while i*i <=x:
            i+=1
        return i-1