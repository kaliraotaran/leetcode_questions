'''
https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack= []

        for asteroid in asteroids:
            res = asteroid
            while stack and stack[-1] > 0 and res<0:
                last= stack.pop()
                if abs(res) == abs(last):
                    res =0 
                elif abs(res)<abs(last):
                    res = last
            if res !=0:
                stack.append(res)
        return stack