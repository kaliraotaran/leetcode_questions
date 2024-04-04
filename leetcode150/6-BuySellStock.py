'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

'''


class solution:
    def sellstocks(self, prices):
        left =0 
        right = 1
        maxp = 0
        while right < len(prices):
            if prices[left]<prices[right]:
                price = prices[right] - prices[left]
                maxp = max(price, maxp)
            else:
                left = right
            right +=1
        return maxp