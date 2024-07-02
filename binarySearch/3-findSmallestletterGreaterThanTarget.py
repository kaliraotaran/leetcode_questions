'''
https://leetcode.com/problems/find-smallest-letter-greater-than-target/submissions/1307367449/?envType=study-plan-v2&envId=binary-search 
'''

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # for i in letters:
        #     if i >target:
        #         return i
        # return letters[0]

        l =0
        r = len(letters)
        while l<r:
            mid = (l+r)//2
            if letters[mid]>target:
                r = mid
            else:
                l =mid+1
        return letters[r] if r<len(letters) else letters[0]