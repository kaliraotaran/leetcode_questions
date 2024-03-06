'''
https://www.codingninjas.com/studio/problems/valid-parenthesis_795104?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION

'''


def isValidParenthesis(s: str) -> bool:
    # Write your code here
    stack = []
    for i in range(len(s)):
        if s[i] in ['[', '{', '(']:
            stack.append(s[i])
        elif s[i] in [']','}', ')']:
            if len(stack ) ==0:
                return False
            else:
                stack.pop(-1)
    if len(stack) ==0 :
        return True
    else:
        return False
    