class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(elems, elemSum, i):
            if elemSum > target or i == len(nums):
                return
            if elemSum == target:
                res.append(elems)
                return
            backtracking(elems+[nums[i]], elemSum+nums[i], i)
            backtracking(elems, elemSum, i+1)
        
        backtracking([], 0, 0)
        return res