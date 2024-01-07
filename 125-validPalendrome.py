# https://leetcode.com/problems/valid-palindrome/

class Solution :
    def valid(self, s:str)->bool:
        newstr = ''

        for c in s:
            if c.isalnum(): # if it is all alpha numeric 
                newstr +=c.lower()
        return newstr == newstr[::-1]
    
sol = Solution()
print(sol.valid('ana'))