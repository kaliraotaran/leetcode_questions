

'''
https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/ 
'''



class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        j = ''
        
        for i in range(len(words)):
            j+= words[i][0]
        if s ==j:
            return True
        return False
        
