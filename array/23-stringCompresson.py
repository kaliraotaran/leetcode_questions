
'''
https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75

'''


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        count = 1
        for j in range(1, len(chars)):
            if chars[j] == chars[j-1]:
                count+=1
            else:
                chars[i] = chars[j-1]
                i+=1
                if count>1:
                    for digits in str(count):
                        chars[i] = digits
                        i+=1
                count =1
        
        chars[i] = chars[-1]
        i+=1
        if count>1:
            for digits in str(count):
                chars[i] = digits
                i+=1
        return i