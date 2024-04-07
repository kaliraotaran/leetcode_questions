'''
https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
     
        sen = s.split()
        return len(sen[-1])