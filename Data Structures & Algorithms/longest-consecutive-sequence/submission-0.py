class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        numset = set(nums)
        heads = set()
        for num in nums:
            if num-1 in numset:
                continue
            else:
                heads.add(num)
        for head in heads:
            long_cons = 1
            while head+long_cons in numset:
                long_cons += 1
            ans = max(ans, long_cons)
        return ans