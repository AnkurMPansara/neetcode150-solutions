class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtracking(part, i):
            if i == len(s):
                res.append(part)
                return
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    backtracking(part+[s[i:j+1]], j+1)
        
        backtracking([], 0)
        return res