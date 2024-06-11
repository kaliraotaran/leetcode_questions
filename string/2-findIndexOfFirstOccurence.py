
'''
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/ 

'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       
        for _ in haystack:
            if needle in haystack:
                return haystack.index(needle)
        return -1