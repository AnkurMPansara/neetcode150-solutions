class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0]*n
        for i in range(m):
            cur = [1]*n
            for j in range(1,n):
                cur[j] = prev[j]+cur[j-1]
            prev = cur
        return prev[-1]