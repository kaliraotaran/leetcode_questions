from typing import List


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         rob1, rob2 = 0,0
#         # [rob1, rob2, n , n+1]
#         for n in nums:
#             temp = max(n+rob1, rob2)
#             rob1 = rob2
#             rob2 = temp
#         return rob2
nums = [2,7,9,3,1]
if not nums:
   print(0)
if len(nums)== 1:
    print(nums[0])

dp1 = [0] * len(nums)
dp2 = [0] * len(nums)

dp1[0] = 0
dp1[1] = nums[0]
dp2[1] = 0
dp2[2] = nums[1]

for i in range(3, len(nums)):
    dp1[i] = max(dp1[i-2] + nums[i-1], dp2[i-1])
    dp2[i] = max(dp1[i-2], dp2[i-2] + nums[i-1])

print( max(dp1[-1], dp2[-1]))