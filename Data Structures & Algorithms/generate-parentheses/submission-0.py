class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(s, openParentheses, totalParentheses):
            if len(s) == 2*n:
                res.append(s)
            if openParentheses > 0:
                backtracking(s+")",openParentheses-1,totalParentheses)
            if totalParentheses < n:
                backtracking(s+"(",openParentheses+1,totalParentheses+1)
        
        backtracking("", 0, 0)
        return res