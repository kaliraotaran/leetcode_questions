# https://leetcode.com/problems/find-the-duplicate-number/

'''
we use a fast and slow pointer 
we assign the slow pointer the value of nums[slow] or nums[0] initialy
and fast pointer nums[nums[fast]] or nums[3 or any pther number in list]
the purpose is to visit random numbers in the list 
we then initialize another pointer slow2
and we apply sort of the same method as above ...
'''
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        
        slow, fast = 0 ,0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow ==slow2:
                break
        return slow

'''
########### antoehr method

        c = Counter(nums)
        for i , j in c.items():
            if j>1:
                return i
            
#################### time excedded
            for i in range(len(nums)):
            c = nums.pop(i)
            if c in nums:
                return c
        return -1
'''