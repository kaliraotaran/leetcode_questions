
'''
https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/1301169842/?envType=study-plan-v2&envId=leetcode-75
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        #we're gonna find the greatest common demo. of the 2 strings

        def gcd(a, b):
            while b:
                a , b = b, a%b
            return a
        
        if str1 +str2 != str2+str1:
            return ''
        
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]
