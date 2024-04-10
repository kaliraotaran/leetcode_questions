'''
https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = s.strip()
        left =0 
        right = len(new)-1
        while left<right:
            if not new[left].isalnum():
                left+=1
                continue
            if not new[right].isalnum():
                right-=1
                continue
            if new[left].lower() == new[right].lower():
                left+=1
                right-=1
            else:
                return False
        return True