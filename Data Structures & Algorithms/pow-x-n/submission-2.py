class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        res = 1
        p = abs(n)
        while p:
            if p%2 == 1:
                res *= x
            x *= x
            p = p//2
        return res if n>0 else 1/res