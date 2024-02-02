# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
'''
we use a simple 2 pointer method in which we set the left pointer at the start of the list and the right pointer right next to it
we the iterate the list while right pointer is less than the length of the array
if the price at teh left pointer is less than price at right of array, we get the difference in the values at those pointers
and the set it to the maxprofit varaible(teh value we set is the maximum of current value we got and teh prev that was already assigned to it)
else: 
the value of left is larger than the right so we move the pointer at left to the position where right pointer is
and then we also keep iterating the right pointer by one anyways
we then return the maximum porfit


'''

class Solution:
    def maxProfit(self, prices:list[int])->int:
        l, r = 0, 1 # the initial starting of the left handside stock and the right handside one
        maxP = 0 # initailly the maximum profit will be 0
        while r<len(prices): 
            if prices[l]<prices[r]:
                price = prices[r]-prices[l]
                maxP = max(price, maxP)
            else:
                l = r
            r+=1
        return maxP
m = Solution()
print(m.maxProfit([7,1,5,3,6,4]))