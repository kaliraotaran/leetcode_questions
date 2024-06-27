'''
https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        slist = list(s)
        left = 0 
        right = len(slist)-1
        vowels = set('aeiouAEIOU')
        while left<right:
            while left<right and slist[left] not in vowels:
                left+=1
            while left<right and slist[right] not in vowels:
                right-=1
            slist[left], slist[right] = slist[right], slist[left]
            left+=1
            right-=1
        return ''.join(slist)
                
                