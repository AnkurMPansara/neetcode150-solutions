class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        res = []
        digitMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        def backtracking(s, i):
            if i == len(digits):
                res.append(s)
                return
            for ch in digitMap[digits[i]]:
                backtracking(s+ch, i+1)
        
        backtracking("", 0)
        return res