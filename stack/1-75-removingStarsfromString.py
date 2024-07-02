

'''
https://leetcode.com/problems/removing-stars-from-a-string/submissions/1307404704/?envType=study-plan-v2&envId=leetcode-75
'''

class Solution:
    def removeStars(self, s: str) -> str:
        a = []
        for i in s:
            if i =="*":
                a.pop()
            else:
                a.append(i)
        return ''.join(a)