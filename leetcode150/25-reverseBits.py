
'''
https://leetcode.com/problems/reverse-bits/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        bi = bin(n).replace('0b', '')[::-1]

        while len(bi)<32:
            bi+='0'
        return int(bi,2)
      