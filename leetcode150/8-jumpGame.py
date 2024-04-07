
'''
https://leetcode.com/problems/jump-game/submissions/1225102928/?envType=study-plan-v2&envId=top-interview-150

here we have to think of it as a car going forward complelty relient on the gas it finds going forward. 
if the gas in the car goes below 0 it cant go forward
else if the new value (new gas can) that we have is greater than the current gas we have, then we take that new
    value of the gas that we found
and we decremnt the gas in our tank by one on each iteration as we move forward

'''

class sol:
    def jumpgame(self, nums):

        gas = 0
        for n in nums:
            if gas<0:
                return False
            elif n>gas:
                gas = n
            gas -=1
        return True
