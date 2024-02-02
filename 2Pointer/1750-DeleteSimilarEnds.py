# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/
'''
2 ptrs left and right
in the question we remove those chars from the string if char at teh left and the right are equal
and also if the char next to it is the same as well
eg. 'aaba' here char at 0 and 4 are same but the char next to 0 is also same, we we will remove that 
            char as well along with the 0 and 4 char

answer in loop
if the element at the left and right pointer are same, and the pointers arent at teh same position
    we will decrement right and incrememtn the left
    we will also store the current char in a variable for next step usage
else:
    we wanna check if the char in current iteration is same as the 
                        prev. char(i mentioned what we wanna do when we encountered this)
        if it is the same we increment or decrement 
        and then we want to continue to next element and check it as well in same iteration
    after that we want to break from the current iteration and move onto the next one

in the end we return the number of elements left in the string which is (right-left )+ 1 
                ( we added the one cause the list started at 0 not 1)


'''
class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s)-1
        currentchar = ''
        while left<=right:
            if (s[left] == s[right] and left !=right):
                currentchar = s[left]
                right -=1
                left+=1
            else:
                if (s[left] == currentchar):
                    left+=1
                    continue
                if s[right] == currentchar:
                    right -=1
                    continue
                break
        return (right - left) + 1



