class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        for i in range(len(s)+1):
            for j in range(len(p)+1):
                if j>0 and p[j-1] == "*":
                    dp[i][j] |= dp[i][j-2]
                    if i>0 and (s[i-1] == p[j-2] or p[j-2] == "."):
                        dp[i][j] |= dp[i-1][j]
                else:
                    if i>0 and j>0 and (s[i-1] == p[j-1] or p[j-1] == "."):
                        dp[i][j] |= dp[i-1][j-1]
        return dp[len(s)][len(p)]