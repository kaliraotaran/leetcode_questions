# https://leetcode.com/problems/ransom-note/description/
'''
here we have 2 lists , ransomnote and magazine
we need to check if a combination of words from the magazine can form the given ransom note
that means all letters present in ransomnote need to be present in magazine
hint:: use replace to remove letters that we already visited
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       
        for i in ransomNote:
            if i not in magazine:
                return False
            magazine = magazine.replace(i,'',1)
        return True
