'''
this is a similar question to trapping rainwater question
In this problem don't think about actaully tarpping water but finding the area of a rectange
(height X width)
so in the math equation that we make, we will first take teh min. of the left pointer and the right pointer 
and then multiply with the width or the area b/w the 2 pointers(right-left)
hence getting the height *width formula (the height will be the min of the 2 pointers cause one side
    of the container cant be heigher than the other, even if it is we take the min. height of the 2)

then we find the maximum from the current area and the prev. calculated area by applying the max() function

after that, we still have to move either the left pointer or the right poitner in each iteration
to do so we can use two conditions:
 if the value at left is less than the value at the right pointer
    move the left  pointer to the next element
 else:
 move the right pointer less one

'''

class Solution:
    def MaxArea(self, height:list[int]):
        left = 0
        right = len(height)-1
        maxx = 0

        while left<right:
            currentsum = min(height[left], height[right]) *(right-left) 
#                               ^^ this is height of rect.  ^^ this would be the width of the rectangle
            maxx = max(currentsum, maxx)
            if height[left]< height[right]:
                left+=1
            else:
                right -=1
        return maxx