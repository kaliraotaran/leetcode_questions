
'''
https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75 
'''

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx =0
        c= 0
        
        for i in range(len(gain)):
            c += gain[i]
            mx = max(c, mx)
        return mx