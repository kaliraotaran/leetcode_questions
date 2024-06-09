
'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1283085911/
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0

        left =0 
        right = 1
        while right<len(prices):
            if prices[left]<prices[right]:
                p += prices[right] -prices[left]
            right+=1
            left+=1
        return p
    