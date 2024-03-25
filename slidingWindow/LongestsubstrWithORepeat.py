# https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
here we use the general sliding window techinique
we first create a variable and make it a set()
we loop through the list with the left pointer starting at left and the right pointer being used as the looping
variable, 
we see if the current char at right is in the set():
    if it is , we remove it from the set and slide teh window to the right by moving left pointer by one
else we're gonna add the current element at right position to the set()
the result and the maximum between the result and length between the left and right pointer(the window size)

'''

class Solution:
    def lengthofSub(self, s:str):

        charset = set()
        left =0 
        res  = 0

        for right in range(len(s)):
            while s[right] in charset: # we check the next element in the string and see if it already exists in set
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
            res = max(res, right -left+1)
        return res

sol = Solution()
print(sol.lengthofSub("abcabcbb"))