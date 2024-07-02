
'''
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/1305110768/?envType=study-plan-v2&envId=leetcode-75 
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = ['a', 'e', 'i', 'o', 'u']
       
        count = sum (1 for char in s[:k] if char in v)

        mcount = count

        for i in range(k, len(s)) :
            if s[i-k] in v:
                count-=1
            if s[i] in v:
                count+=1
            if (mcount <count):
                mcount = count
        return mcount      