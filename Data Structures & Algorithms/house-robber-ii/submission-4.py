class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [[-1, -1] for i in range(len(nums))]
        dp[0] = [nums[0], 0]
        dp[1] = [max(nums[0], nums[1]), nums[1]]

        for i in range(2, len(nums)):
            dp[i][0] = max(dp[i-1][0], nums[i]+dp[i-2][0])
            dp[i][1] = max(dp[i-1][1], nums[i]+dp[i-2][1])
        
        return max(dp[len(nums)-2][0], dp[len(nums)-1][1])

