

'''
https://leetcode.com/problems/longest-common-prefix/submissions/1284079458/
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
         
        s = ''
        strs.sort()

        for i in range(len(min(strs))):
            if strs[0][i] == strs[-1][i]:
                s+=strs[0][i]
            else:
                break
        return s
