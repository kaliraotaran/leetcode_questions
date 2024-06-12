
'''
https://leetcode.com/problems/shuffle-string/
'''

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
 
        s1 = ''
        for i in range(len(s)):
            s1+= s[indices.index(i)]
        return s1
