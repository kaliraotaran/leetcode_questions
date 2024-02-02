# https://leetcode.com/problems/valid-palindrome/
'''
there are multiple solutions to this simple problem, 
we initailize an empty string 
and then we start looping through the string 
we then add every character to the new string that is only alpha numberic (.isalnum()) and we add then one by 
one in lower case
we then return true if the reverse of the new string is equal to the normal new string



'''
class Solution :
    def valid(self, s:str)->bool:
        newstr = ''

        # for c in s:
        #     if c.isalnum(): # if it is all alpha numeric 
        #         newstr +=c.lower()
        # return newstr == newstr[::-1]
        
        
            
    
sol = Solution()
print(sol.valid('ana'))
 