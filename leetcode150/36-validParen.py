

'''
https://leetcode.com/problems/valid-parentheses/submissions/1240076578/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if not stack:
                    return False
                currentchar = stack.pop()
                if currentchar =='(':
                    if i !=')':
                        return False
                if currentchar =='{':
                    if i !='}':
                        return False
                if currentchar =='[':
                    if i !=']':
                        return False
        if stack:
            return False
        else:
            return True