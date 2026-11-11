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


#### another simple solutiom , since we can't just compare
# toady and then tomorrow, we just compare the current day with yesterday and if yesterday 
# was lower then today, that means we can get a profit. 

    profit =0
    for i in range(1, len(prices)):
        if prices[i]>prices[i-1]:
            profit += prices[i]-prices[i-1]