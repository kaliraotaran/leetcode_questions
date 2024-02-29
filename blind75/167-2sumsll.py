# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1130782545/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l<r:
            cursum = numbers[l]+numbers[r]
            if cursum >target:
                r-=1
            elif cursum <target:
                l+=1
            else:
                return [l+1, r+1]
        return []