class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            if (i, j) not in dp:
                if j + 1 < len(p) and p[j+1] == "*":
                    if i < len(s) and (s[i] == p[j] or p[j] == "."):
                        dp[(i,j)] = dfs(i, j + 2) or dfs(i + 1, j)
                    else:
                        dp[(i,j)] = dfs(i, j + 2)
                else:
                    if i < len(s) and (s[i] == p[j] or p[j] == "."):
                        dp[(i,j)] = dfs(i + 1, j + 1)
                    else:
                        dp[(i,j)] = False
            return dp[(i,j)]
        return dfs(0, 0)