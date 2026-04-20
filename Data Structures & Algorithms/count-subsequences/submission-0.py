class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1]*(len(t)+1) for _ in range(len(s)+1)]

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if dp[i][j] == -1:
                if s[i] == t[j]:
                    dp[i][j] = dfs(i+1,j+1) + dfs(i+1,j)
                else:
                    dp[i][j] = dfs(i+1,j)
            return dp[i][j]
        
        return dfs(0,0)