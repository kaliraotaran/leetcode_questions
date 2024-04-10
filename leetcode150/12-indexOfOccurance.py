'''

.https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/1228847329/?envType=study-plan-v2&envId=top-interview-150'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in haystack:
            if needle in haystack:
                return haystack.index(needle)
            else:
                return -1