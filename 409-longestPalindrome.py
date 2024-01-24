# https://leetcode.com/problems/longest-palindrome/
'''
we dont actaully have to form the palindrome, we can just count the number of
letters to see if they're a pair(even)
we use a hashmap to assign the number of occurance of that letter in the string
and then we have a list and a var odd, list holds all the values of the keys 
    from hashtable(teh actual number of occurances of all letters)
if the val is odd (means %2 !=0) then we increment odd's value
in the end, if odd !=0 , we return the sum of values in list -odd +1
    (we added one cause there could be one odd letter in middle of palendrome)
else we return teh normal sum of list

'''
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