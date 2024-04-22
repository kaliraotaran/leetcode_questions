
'''
https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        currentNumber = n
        number =0
        hash = {}

        while True:
            for i in str(currentNumber):
                number+= int(i) **2
            if number ==1:
                return True
            if number in hash:
                return False
            hash[number] =0 
            currentNumber = number
            number = 0