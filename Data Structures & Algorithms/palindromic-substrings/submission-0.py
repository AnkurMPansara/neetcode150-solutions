class Solution:
    def countSubstrings(self, s: str) -> str:
        if not s:
            return 0
        res = 0
        dp = [[False]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            res += 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res += 1
        for k in range(3, len(s)+1):
            for i in range(len(s)-k+1):
                j = i + k - 1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    res += 1
        return res