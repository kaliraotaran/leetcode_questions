# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isvalid(self, s:str)->bool:
        stack = []
        closeToOpen = {"}":"{", "]":"[", ")":"("}

        for c in s:
            if c in closeToOpen:
                if stack or stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else  False
sol = Solution()
print(sol.isvalid("(){"))