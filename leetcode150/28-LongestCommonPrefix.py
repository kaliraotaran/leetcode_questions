
'''
https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150'
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        ans = ''
        strs = sorted(strs)

        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first), len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans