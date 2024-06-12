

'''
https://leetcode.com/problems/split-a-string-in-balanced-strings/ 
'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        for i in s:
            if i == 'R':
                r+=1
            if i =='L':
                l+=1
            if r==l:
                res +=1
        return res
        