'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1223359297/?envType=study-plan-v2&envId=top-interview-150
'''

class sol:
    def stock2(self, prices):
        left =0 
        right =1
        profit =0 
        while right<len(prices):
            if prices[left]<prices[right]:
                profit += prices[right]-prices[left]
            left+=1
            right+=1
        return profit