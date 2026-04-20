class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0]*(len(t)+1)
        dp[0] = 1

        for i in range(1, len(s)+1):
            nxt = 1
            for j in range(1, len(t)+1):
                res = dp[j]
                if s[i-1] == t[j-1]:
                    dp[j] += nxt
                nxt = res
        return dp[len(t)]