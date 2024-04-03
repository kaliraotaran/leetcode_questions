'''
https://leetcode.com/problems/remove-element/submissions/1222367015/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)