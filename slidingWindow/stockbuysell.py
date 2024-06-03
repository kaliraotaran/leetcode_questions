
'''

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

here, we also use some knowloedge from teh 2 ptr method, 
we set the left ptr at 0 and teh right at 1 
and we keep iterating the list as long as the right ptr doesn't exceed the len. of list
if the value at the left is greater than value on right(that means we're getting a loss on the stock) we move the left ptr to right position and iterate right
else we check if the value at left is less than value at right pointer(means we're gonna get a profit), then we get teh current profit by doing prices[r]-prices[l] and
then we find the maxi. profit by comparing it with previous sums that we calculated for 
other profits that we could have taken
'''


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
       
        l = 0 
        r = 1
        maxp = 0
        while r<len(prices):
            if prices[l]<prices[r]:
                curr = prices[r]-prices[l]
                maxp = max(curr, maxp)
            else:
                l = r 
            r+=1
        return maxp

