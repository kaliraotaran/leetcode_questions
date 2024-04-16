

'''
https://leetcode.com/problems/ransom-note/submissions/1234198066/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = {}
        for i in magazine:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] +=1
        for i in ransomNote:
            if i in hash and hash[i]>0:
                hash[i] -= 1
            else:
                return False
        return True