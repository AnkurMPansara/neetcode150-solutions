class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        prev = [False]*(len(p)+1)
        prev[0] = True
        for i in range(len(s)+1):
            cur = [False]*(len(p)+1)
            if i == 0:
                cur[0] = True
            for j in range(len(p)+1):
                if j>0 and p[j-1] == "*":
                    cur[j] |= cur[j-2]
                    if i>0 and (s[i-1] == p[j-2] or p[j-2] == "."):
                        cur[j] |= prev[j]
                else:
                    if i>0 and j>0 and (s[i-1] == p[j-1] or p[j-1] == "."):
                        cur[j] |= prev[j-1]
            prev = cur
        return prev[len(p)]