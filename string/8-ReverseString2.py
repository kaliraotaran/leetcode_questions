'''
https://leetcode.com/problems/reverse-string-ii/ 
'''


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        l = 0 
        r = min(k, len(s))

        while l <len(s):
            s = s[:l]+ s[l:r][::-1] + s[r:]

            l += 2*k
            r = min(l+k, len(s))
        return s
