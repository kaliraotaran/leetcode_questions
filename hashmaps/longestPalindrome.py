'''
https://leetcode.com/problems/longest-palindrome/submissions/1187972357/

'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
       
        hasht = {}
        odd =0
        summ = []
        for i in s:
            if i not in hasht:
                hasht[i] = 1
            else:
                if i in hasht:
                    hasht[i]+=1
        for values in hasht.values():
            summ.append(values)
            if values %2 !=0:
                odd += 1
        if odd !=0:
            return sum(summ)-odd +1
        else:
            return sum(summ)
       
       
        
       
       
       
       
       
       
       
       