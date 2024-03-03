

'''
https://www.codingninjas.com/studio/problems/stocks-are-profitable_893405?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
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