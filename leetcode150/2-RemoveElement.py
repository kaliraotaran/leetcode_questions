'''
https://leetcode.com/problems/remove-element/submissions/1222367015/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Two-pointer approach:
        - Use a slow pointer to track the position to overwrite
        - Use a fast pointer to scan through the array
        - Keep only elements that are NOT equal to val
        """
        k = 0  # count of elements != val (this will be our new length)

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        # After this loop:
        # - nums[0..k-1] contains all elements != val (order may change)
        # - nums[k..] contains the remaining elements (can be ignored)
        # - k is the new length to return

        return k