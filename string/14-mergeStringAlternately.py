

'''
https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
'''


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        n= min(len(word1), len(word2))
        for i in range(n):
            s+= word1[i]+word2[i]

        if len(word1)> len(word2):
            s+= word1[n:]
        else:
            s+= word2[n:]
        return s



