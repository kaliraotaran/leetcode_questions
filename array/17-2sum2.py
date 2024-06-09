
'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ 
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        left =0 
        right = len(numbers)-1
        while left<right:
            summ =numbers[right]+numbers[left] 
            if  summ> target:
                right-=1
            elif summ<target:
                left+=1
            else:
                return [left+1, right+1]
