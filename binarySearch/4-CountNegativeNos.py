'''
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/1307386175/?envType=study-plan-v2&envId=binary-search 
'''

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count =0
        cols = len(grid[0])
        rows = len(grid)

        i =rows-1
        j = 0

        while i>=0 and j <cols:
            if grid[i][j]<0:
                count+=(cols-j)
                i-=1
            else:
                j+=1
        return count
        