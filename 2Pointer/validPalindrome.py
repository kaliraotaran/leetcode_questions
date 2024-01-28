
'''
pretty staright forward implementation of 2ptr method

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        while left<right:
            if not s[left].isalnum() :# this checks if the current element is an alphanumeric value 
                left+=1
                continue # after going to the next valid letter, we still want to continue 
                            # with execution of same iteration of loop
            if not s[right].isalnum():
                right -=1
                continue
            if s[left].lower()== s[right].lower():
                left+=1
                right-=1
            else:
                return False
        return True



        # newstr = ''
        # for c in s:
        #     if c.isalnum():
        #         newstr+=c.lower()
        # return newstr[::-1] == newstr[::]
        






















        # newstr = ''

        # for c in s:
        #     if c.isalnum():
        #         newstr +=c.lower()
        # return newstr == newstr[::-1]
