class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*2 for i in range(len(prices))]
        
        for i in range(len(prices)-1, -1, -1):
            #can Buy stock
            buy = dp[i+1][0] - prices[i] if i+1<len(prices) else -prices[i]
            wait = dp[i+1][1] if i+1<len(prices) else 0
            dp[i][1] = max(buy, wait)
            #cant buy stock
            sell = dp[i+2][1] + prices[i] if i+2<len(prices) else prices[i]
            wait = dp[i+1][0] if i+1<len(prices) else 0
            dp[i][0] = max(sell, wait)
        
        return dp[0][1]