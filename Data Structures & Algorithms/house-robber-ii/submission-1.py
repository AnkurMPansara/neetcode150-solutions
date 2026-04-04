class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [[-1, -1] for i in range(len(nums))]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums)-1):
                return 0
            if dp[i][flag] == -1:
                dp[i][flag] = max(dfs(i+1, flag), nums[i] + dfs(i+2, flag))
            return dp[i][flag]
        
        return max(dfs(0, 1), dfs(1, 0))

