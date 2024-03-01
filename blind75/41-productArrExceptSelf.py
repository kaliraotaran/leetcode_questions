# 
'''
https://leetcode.com/problems/product-of-array-except-self/submissions/1133215642/

'''

class Solution:
    def pro(self, nums: list[int])->list[int]:
        length = len(nums)
        products = [1]*length
        for i in range(1, length): #  we start from 1 not 0 cause we skip the first element for now
            products[i] = nums[i-1]*products[i-1]
        right = nums[-1]
        for i in range(length-2, -1, -1):
            products[i]*=right # now we go from right to left
            right *= nums[i]
        return products
p = Solution()
print(p.pro([1,2,3,4]))