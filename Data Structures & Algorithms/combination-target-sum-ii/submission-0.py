class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtracking(elems, elemSum, i):
            if elemSum >= target or i == len(candidates):
                if elemSum == target:
                    res.append(elems)
                return
            backtracking(elems+[candidates[i]], elemSum+candidates[i], i+1)
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtracking(elems, elemSum, i+1)
        
        backtracking([], 0, 0)
        return list(res)