
'''
https://leetcode.com/problems/remove-outermost-parentheses/



'''

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        Popen = 0
        result =[]

        for i in s:
            if i ==')':
                Popen -=1
            if Popen>0:
                result.append(i)
            if i == '(':
                Popen +=1
        return ''.join(result)
