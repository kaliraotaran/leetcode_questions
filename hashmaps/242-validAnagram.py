'''
https://leetcode.com/problems/valid-anagram/description/
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countt, counts = {},{}

        for i in t:
            if i not in countt:
                countt[i] =1
            else:
                if i in countt:
                    countt[i]+=1
        for i in s:
            if i not in counts:
                counts[i]=1
            else:
                if i in counts:
                    counts[i]+=1
        if countt !=counts:
            return False
        return True