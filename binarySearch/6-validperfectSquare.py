'''
https://leetcode.com/problems/valid-perfect-square/?envType=study-plan-v2&envId=binary-search 
'''



class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num ==1:
            return True
        for i in range(num):
            if i*i == num:
                return True
            if i*i >num:
                return False
        return False
