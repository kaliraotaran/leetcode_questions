'''
https://leetcode.com/problems/find-the-difference/
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tableS = {}
        tableT = {}

        for i in s:
            if i not in tableS:
                tableS[i]=1
            else:
                if i in tableS:
                    tableS[i]+=1
        for i in t:
            if i not in tableT:
                tableT[i]=1
            else:
                if i in tableT:
                    tableT[i]+=1
        for char in tableT:
            if char not in tableS or tableT[char]> tableS[char]:
                return char
                
