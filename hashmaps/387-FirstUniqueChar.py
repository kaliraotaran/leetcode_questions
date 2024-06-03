
'''
https://leetcode.com/problems/first-unique-character-in-a-string/
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
       
        for i in s:
            if i not in hashmap:
                hashmap[i] =1
            else:
                if i in hashmap:
                    hashmap[i]+=1
        for i in range(len(s)):
            if hashmap[s[i]] ==1: 
                return i
        '''
        or
        for keys, values in hash.items():
            if values ==1:
                return s.index(keys)
                break
                
        '''
        return -1
    

        
        