

'''
https://leetcode.com/problems/shuffle-string/description/

here, we first create a new list of chracter of the same length as teh given string

we then place the letter at that index of teh new list of  characters in the position it should be if the original string was shuffled randomly. 
for ex. shuffle = [0,2,1] s = 'acb'
 a[suffle[i]] = s[i]
 a[0](0) = a
 a[1](2) = c ( so here we placed the character b at the 2 index instead of the 1th index)

 and then in the end we concat list into a string 

'''

class Solution:
    def shuffle(self, s:str, indices: list):
        a = ['']*len(s)
        for i in range(len(s)):
            a[indices[i]] = s[i]
        return ''.join(a)

