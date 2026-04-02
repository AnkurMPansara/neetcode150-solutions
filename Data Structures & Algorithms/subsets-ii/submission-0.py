class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtracking(subset, i):
            if i == len(nums):
                res.append(subset)
                return
            backtracking(subset+[nums[i]], i+1)
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtracking(subset, i+1)
        
        backtracking([], 0)
        return res