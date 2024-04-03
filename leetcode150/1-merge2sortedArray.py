'''
https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, n+m):
            nums1[i] = nums2[i-m]
        return nums1.sort()