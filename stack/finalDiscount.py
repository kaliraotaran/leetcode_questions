
'''
https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/submissions/1196969196/
'''

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack  = []

        for i in range(len(prices)):
            while stack and (prices[stack[-1]]>= prices[i]):
                prices[stack.pop()] -= prices[i]
            stack.append(i)
        return prices

