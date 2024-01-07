# https://leetcode.com/problems/ransom-note/description/

class Solution:
    def cann(self, ransomNote: str, magazine:str)->bool:
        for i in ransomNote: # we start taking each letter in the ransomnote to compare
            if i not in magazine:   # if the certain letter isnt present in magazine, return false
                return False
            magazine = magazine.replace(i ,'', 1) # this means that it is present and we want to bascially delete it, 
                                    # if we delete the whole string, it means all letters we're present in magazine and return true
        return True
    
print(Solution().cann('aab','aaxxb'))