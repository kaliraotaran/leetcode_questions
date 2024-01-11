# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        ans = []
        odd =0

        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] +=1
        for times in count.values():
            ans.append(times)
            if times %2 !=0:
                odd +=1
        if odd !=0:
            return sum(ans) - odd +1
        elif odd ==0:
            return sum(ans)-odd