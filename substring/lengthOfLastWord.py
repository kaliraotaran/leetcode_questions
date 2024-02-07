

'''
https://leetcode.com/problems/length-of-last-word/description/

we first strip the string of any unwanted spaces before and after the words
then we assign the value of s as its reverse
we initialize a variable c with value 0
and then we starting iterating the string s
if at each time the character is not ' ', we add one to c, which means it's part of a word
but if we encounter a ' ', we break because it means we are about the start the next word
and then we just return c in the end 


'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s[::-1]
        c = 0
        for i in s:
            if (i != ' '):
                c+=1
            else:
                break
        return c