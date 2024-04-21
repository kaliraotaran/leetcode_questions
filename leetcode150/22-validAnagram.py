'''
https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        for i in s:
            if i not in hash1:
                hash1[i]= 1
            else:
                hash1[i]+=1
        for i in t:
            if i not in hash2:
                hash2[i] = 1
            else:
                hash2[i]+=1
        if hash1 != hash2:
            return False
        else:
            return True