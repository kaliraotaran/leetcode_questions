
'''
https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        new = ''
        for i in s[::-1]:
            new+= i
            new+=' '
        return new.strip()