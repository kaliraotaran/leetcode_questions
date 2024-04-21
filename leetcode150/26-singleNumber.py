
'''
https://leetcode.com/problems/single-number/submissions/1238091234/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        hash = {}

        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i]+=1
        for keys, values in hash.items():
            if values ==1:
                return keys