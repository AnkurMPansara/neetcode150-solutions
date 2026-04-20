class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        prev = defaultdict(int)
        prev[0] = 1

        for i in range(len(nums)):
            cur = defaultdict(int)
            for t, c in prev.items():
                cur[t + nums[i]] += c
                cur[t - nums[i]] += c
            prev = cur
        
        return prev[target]