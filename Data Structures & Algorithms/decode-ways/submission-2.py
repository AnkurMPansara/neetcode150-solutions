class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        dp = [0]*len(s)
        dp[0] = 1
        if s[0] == "1":
            dp[1] += 1
        if s[0] == "2" and s[1] in "0123456":
            dp[1] += 1
        if s[1] != "0":
            dp[1] += 1

        for i in range(2, len(s)):
            if s[i-1] == "1":
                if s[i] == "0":
                    dp[i] = dp[i-2]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
            elif s[i-1] == "2" and s[i] in "0123456":
                if s[i] == "0":
                    dp[i] = dp[i-2]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
            else:
                if s[i] == "0":
                    dp[i] = 0
                else:
                    dp[i] = dp[i-1]
        
        return dp[-1]
