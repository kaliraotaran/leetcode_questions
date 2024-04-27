

'''
https://leetcode.com/problems/longest-consecutive-sequence/submissions/1243462768/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums)
        new = list(new)
        new.sort()
        count = 0
        temp = 1
        new.append(None)
        for i in range(len(new)-1):
            if new[i]+1 == new[i+1]:
                temp+=1
            else:
                count = max(count, temp)
                temp =1
         
        return count