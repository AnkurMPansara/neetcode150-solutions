class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1) for i in range(len(coins)+1)]
        coins.sort()

        for i in range(len(coins)+1):
            dp[i][0] = 1
        
        for i in range(len(coins)):
            for a in range(1, amount+1):
                dp[i+1][a] = dp[i][a]
                if a >= coins[i]:
                    dp[i+1][a] += dp[i+1][a-coins[i]]
        
        return dp[-1][amount]