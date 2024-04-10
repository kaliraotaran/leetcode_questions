
'''
https://leetcode.com/problems/is-subsequence/submissions/1228854973/?envType=study-plan-v2&envId=top-interview-150

here we're gonna run 2 pointers at the same time and the first pointer tracks progress in the first string and
the second pointer in teh second string. 

'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i =0 
        j =0 
        while i <len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        if i== len(s):
            return True
        else:
            return False
