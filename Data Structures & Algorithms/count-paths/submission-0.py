class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for i in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        def dfs(i, j):
            if i<0 or j<0:
                return 0
            if dp[i][j] == -1:
                dp[i][j] = dfs(i-1,j) + dfs(i,j-1)
            return dp[i][j]
        
        return dfs(m-1, n-1)