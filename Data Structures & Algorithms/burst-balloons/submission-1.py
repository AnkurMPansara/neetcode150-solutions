class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = [[-1]*(len(nums)) for _ in range(len(nums))]
        def dfs(l, r):
            if l > r:
                return 0
            if dp[l][r] == -1:
                left = nums[l-1] if l > 0 else 1
                right = nums[r+1] if r < len(nums) -1 else 1
                res = 0
                for i in range(l, r+1):
                    res = max(res, dfs(l, i-1) + left*nums[i]*right + dfs(i+1,r))
                dp[l][r] = res
            return dp[l][r]
        return dfs(0,len(nums)-1)