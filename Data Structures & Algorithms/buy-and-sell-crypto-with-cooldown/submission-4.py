class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        dp1 = [max(0, prices[1]-prices[0]), max(-prices[0],-prices[1])]
        dp2 = [0, -prices[0]]
        
        for i in range(2,len(prices)):
            dp0 = [0,0]
            #holding a stock
            dp0[1] = max(dp1[1], dp2[0]-prices[i])
            #am free
            dp0[0] = max(dp1[0], dp1[1]+prices[i])
            dp1, dp2 = dp0, dp1
        
        return max(dp1)