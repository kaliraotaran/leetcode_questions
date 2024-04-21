

'''
https://leetcode.com/problems/word-pattern/submissions/1234811233/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        mapping = {}
        for i in range(len(pattern)):
            if pattern[i] in mapping:
                if mapping[pattern[i]] != words[i]:
                    return False
                
            else:
                if words[i] in mapping.values():
                    return False
                mapping[pattern[i]] = words[i]
        return True