class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1]*2 for i in range(len(prices))]
        
        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if dp[i][canBuy] == -1:
                waiting = dfs(i+1, canBuy)
                if canBuy:
                #actions -> buy, wait
                    buy = dfs(i+1, False) - prices[i]
                    dp[i][canBuy] = max(buy, waiting)
                else:
                #sell, wait
                    sell = dfs(i+2, True) + prices[i]
                    dp[i][canBuy] = max(sell, waiting)
            return dp[i][canBuy]
        
        return dfs(0, True)