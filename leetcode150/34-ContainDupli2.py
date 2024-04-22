
'''
https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}

        for i in range(len(nums)):
            if nums[i] in hash:
                if abs(hash[nums[i]] - i)<= k:
                    return True
            hash[nums[i]] = i
        return False
        