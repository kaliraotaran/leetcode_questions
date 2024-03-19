

'''
https://www.codingninjas.com/studio/problems/reverse-stack-using-recursion_631875?interviewProblemRedirection=true&leftPanelTabValue=DISCUSS
'''

def reversestack(stack):


    def rev(stack, left, right):
        if left>=right:
            return stack
        else:
            stack[left], stack[right] = stack[right], stack[left]
        return rev(stack=stack,left= left+1, right = right-1)
    
    stack = rev(stack=stack, left=0, right=len(stack)-1)
    return stack