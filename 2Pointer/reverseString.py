# https://leetcode.com/problems/reverse-string/description/

'''


here we use a very simple version of 2 pointer
we set the 2 ptrs normally and then set the while loop up
and we just swap the chars left and right postion and increment left 
and decrement right


'''




class Solution:
    def reverse(self, s:list[str]):
        left = 0
        right = len(s)-1
        while left<=right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -=1
        return s
    



    
sol = Solution()
s = ['t','a','r','a','n']
print(sol.reverse(s))