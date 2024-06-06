
'''

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1279793259/
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l= 0 
        r = 1

        maxp  =0 

        while r<len(prices):
            if prices[l]<prices[r]:
                cur = prices[r]-prices[l]
                maxp = max(cur, maxp)
            else:
                l = r
            r+=1
        return maxp
    