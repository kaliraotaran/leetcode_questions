'''
https://leetcode.com/problems/palindrome-number/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = str(x)
        left = 0 
        right = len(st)-1
        while left<right:
            if st[left] == st[right]:
                left+=1
                right-=1
            else:
                return False
        return True