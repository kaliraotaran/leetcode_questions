

'''
https://leetcode.com/problems/valid-parentheses/submissions/1196944571/
'''
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for i in s:
            if i in ['[', '{', '(']:
                stack.append(i)
            else:
                # meaning if stack contains just a closing paren cause it wasnt in the above statment
                if not stack:
                    return False
                currentchar = stack.pop()
                if currentchar == '(':
                    if i !=')':
                        return False
                if currentchar =='{':
                    if i != '}':
                        return False
                if currentchar =='[':
                    if i != ']':
                        return False
        if stack:
            return False
        else:
            return True
 




