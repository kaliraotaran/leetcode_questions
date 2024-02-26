


'''
https://leetcode.com/problems/single-number/description/
'''

class Solution:
    def single(self, nums: list[int]) -> int:

        dictt = {}

        for i in nums:
            if i not in dictt:
                dictt[i] =1
            else:
                if i in dictt:
                    dictt[i]-=1
        for key, value in  dictt.items():
            if value ==1 :
                return key