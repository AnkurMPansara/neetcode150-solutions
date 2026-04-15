class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        bit = 1
        for i in range(32):
            if n & bit:
                res += 1
            bit = bit << 1
        return res