

'''
https://leetcode.com/problems/is-subsequence/submissions/1302839407/?envType=study-plan-v2&envId=leetcode-75 
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i =0
        j = 0

        while i <len(s) and j<len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        if i == len(s):
            return True
        return False
   
