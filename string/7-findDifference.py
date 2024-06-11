
'''
https://leetcode.com/problems/find-the-difference/ 
'''


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        if len(t)> len(s):
            for i in t:
                if t.count(i) > s.count(i):
                    return i