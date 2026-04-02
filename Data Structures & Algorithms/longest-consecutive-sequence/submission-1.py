class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        numset = set(nums)
        for num in nums:
            if num-1 not in numset:
                long_cons = 1
                while num+long_cons in numset:
                    long_cons += 1
                ans = max(ans, long_cons)
        return ans