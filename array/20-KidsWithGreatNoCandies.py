'''
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/1301180999/?envType=study-plan-v2&envId=leetcode-75
'''


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr = []*len(candies)

        for i in candies:
            if i+extraCandies >= max(candies):
                arr.append(True)
            else:
                arr.append(False)
        return arr
