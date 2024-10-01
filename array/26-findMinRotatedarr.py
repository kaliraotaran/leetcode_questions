
'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we sort the list first using quick sort since its n log n 
        def quicksort(nums):
            l= len(nums)

            if l<=1:
                return nums
            else:
                pivot = nums.pop()

            ig = []
            il = []

            for i in nums:
                if i >pivot:
                    ig.append(i)
                else:
                    il.append(i)
            return quicksort(il)+[pivot]+quicksort(ig)
        n = quicksort(nums)
        # then we just print the first element of the sorted array since its smallest
        return n[0]