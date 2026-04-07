class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        res = s[0]
        maxLen = 0
        dp = [[False]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                if maxLen < 2:
                    maxLen = 2
                    res = s[i:i+2]
        for k in range(3, len(s)+1):
            for i in range(len(s)-k+1):
                j = i + k - 1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    if k > maxLen:
                        maxLen = k
                        res = s[i:i+k]
        return res
        