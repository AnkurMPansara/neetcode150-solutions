class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        dp = [[-1]*len(matrix[0]) for _ in range(len(matrix))]
        def dfs(i, j, prev):
            if i<0 or i==len(matrix) or j<0 or j==len(matrix[0]) or matrix[i][j] <= prev:
                return 0
            if dp[i][j] == -1:
                res = 1
                for dx, dy in directions:
                    res = max(res, 1+dfs(i+dx, j+dy, matrix[i][j]))
                dp[i][j] = res
            return dp[i][j]
        
        LIS = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                LIS = max(LIS, dfs(i,j,-1))
        return LIS
