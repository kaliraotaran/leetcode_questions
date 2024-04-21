'''
https://leetcode.com/problems/plus-one/submissions/1238069036/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      
        s = map(str, digits)
        s = ''.join(s)
        s = int(s)
        s+=1
        s = str(s)
        s = list(s)
        newlist = []
        for i in s:
            newlist.append(int(i))
        return newlist