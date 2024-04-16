
'''
https://leetcode.com/problems/container-with-most-water/submissions/1230586732/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left =0
        right = len(height)-1

        maxx =0

        while left<right:
            summ = min(height[right], height[left]) *(right -left)
            maxx = max(summ, maxx)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxx