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
print(sol.isvalid("(){}"))

# or
#   stack = []
        # for c in s:
        #     if c == "(" or c == "[" or c == "{":
        #         stack.append(c)
        #     elif len(stack) == 0:
        #         return False
        #     else:
        #         stackC = stack.pop()
        #         if c == ")" and stackC == "(":
        #             continue
        #         if c == "]" and stackC == "[":
        #             continue
        #         if c == "}" and stackC == "{":
        #             continue
        #         return False
        # if len(stack) == 0:
        #     return True
        # return False