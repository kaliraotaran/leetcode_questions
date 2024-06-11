
'''
https://leetcode.com/problems/isomorphic-strings/
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        slist = []
        tlist = []

        for i in s:
            slist.append(s.index(i))
        for i in t:
            tlist.append(t.index(i))
        if slist == tlist :
            return True
        return False
        
