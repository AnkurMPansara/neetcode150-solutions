class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0]*(n+2) for _ in range(n+2)]
        for r in range(1,n+2):
            for l in range(r-1,-1,-1):
                for i in range(l+1,r):
                    coins = nums[l] * nums[i] * nums[r]
                    dp[l][r] = max(dp[l][r], dp[l][i] + dp[i][r] + coins)
        return dp[0][n+1]

