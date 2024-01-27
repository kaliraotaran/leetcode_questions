# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/

'''
we have a list, and ew first will sort it 
the question states that we need to find those subsequencies such that they
add upto or less than the target
the question also states that we need to modulo the answer at the end 
        with (10^9 +7) cause the answer may be too large
we're gonna use 2 ptrs left and right
left is always smaller than right
if the addition of the left and right pointer is > target, we move right ptr left 1
else we'll perform following operation pow(2,(right-left), modulo function)
    (the pow takes 3 params so it'll be(2^(right-left) % modulo) ) )
and then we add it to the result
we than increment left by 1
and keep doing the same opeartion until we break out of loop
in the end we return the result % modulo, 
(the modulo really doesnt effect the result cause its value is 10000007 and 
for ex. 12 %10000007 is still 12)
    
'''

class Solution:
    def numseq(self, nums:list[int], target:int):
        result = 0
        right = len(nums)-1
        left = 0
        nums.sort()
        mod = (10**9)+7

        while left<=right:
            if nums[left]+nums[right] > target:
                right -=1
            else:
                result += pow(2, (right -left), mod)
                left +=1
        return result % mod
    




sol = Solution()
print(sol.numseq([3,5,6,7], 9))