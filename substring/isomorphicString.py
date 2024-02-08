'''
https://leetcode.com/problems/isomorphic-strings/description/

we're gonna initlialize 2 lists, 
and then iterate each string and only add the index of i'th letter in the string 
for eg. s = egg, the list of indexes for this would be [0,1,1] beaucse g are repeated twice
and then we just return true if the list of both the strings are the same
else false


'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        listS = []
        listT = []

        for i in s:
           listS.append(s.index(i))
        for i in t:
            listT.append(t.index(i))
        
        if listT == listS:
            return True
        else:
            return False