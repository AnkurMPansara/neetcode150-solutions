class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(prev, i):
            if i == len(nums):
                res.append(prev)
                return
            backtracking(prev,i+1)
            backtracking(prev+[nums[i]],i+1)
        
        backtracking([], 0)
        return res
