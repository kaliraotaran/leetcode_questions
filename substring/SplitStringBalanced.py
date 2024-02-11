
'''
https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

here the main goal is to see if the given string can be split into how many parts such that the parts
are balanced
so we start by iterating through the string:
if we encounter a L , we increment the L variable
if we encounter an R, we increment the R variable
and after increment, if the value of L and R match, that means there a pair the exists at that moment, we we add 1 to result variable


'''

class Solution:
    def balanced(self, s: str):
        ans = 0
        l, r = 0, 0
        for i in s:
            if i=='R':r+=1
            if i=='L': l+=1
            if l==r: ans +=1
        return ans
