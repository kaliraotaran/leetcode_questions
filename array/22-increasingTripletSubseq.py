
'''
https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = float('inf')
        second = float('inf')

        for third in nums:
            if second< third:return True
            if third<= first: first = third
            else:
                second = third
        return False