class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(cur, candidates):
            if len(cur) == len(nums):
                res.append(cur)
                return
            for i in range(len(candidates)):
                backtracking(cur+[candidates[i]],candidates[:i]+candidates[i+1:])
        
        backtracking([], nums)
        return res