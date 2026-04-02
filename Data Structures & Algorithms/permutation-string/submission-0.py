class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charmap1 = {}
        for c in s1:
            charmap1[c] = charmap1.get(c, 0) + 1
        l = 0
        charmap2 = {}
        for r in range(len(s2)):
            charmap2[s2[r]] = charmap2.get(s2[r], 0) + 1
            while len(s1) < (r-l+1):
                charmap2[s2[l]] -= 1
                if charmap2[s2[l]] == 0:
                    del charmap2[s2[l]]
                l += 1
            if charmap1 == charmap2:
                return True
        return False
            
        