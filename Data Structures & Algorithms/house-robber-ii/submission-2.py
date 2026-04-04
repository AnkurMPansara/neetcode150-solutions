class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [[-1, -1] for i in range(len(nums))]

        def dfs(i, flag):
            if i < 0:
                return 0
            if i == 0:
                return nums[0] if flag else 0
            if dp[i][flag] == -1:
                dp[i][flag] = max(dfs(i-1, flag), nums[i] + dfs(i-2, flag))
            return dp[i][flag]
        
        return max(dfs(len(nums)-1, 0), dfs(len(nums)-2, 1))

