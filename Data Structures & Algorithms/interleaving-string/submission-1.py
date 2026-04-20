class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        prev = [False]*(len(s2)+1)
        prev[0] = True

        for i in range(len(s1)+1):
            cur = [False]*(len(s2)+1)
            if i==0:
                cur[0] = True
            for j in range(len(s2)+1):
                if i>0 and s1[i-1] == s3[i+j-1]:
                    cur[j] |= prev[j]
                if j>0 and s2[j-1] == s3[i+j-1]:
                    cur[j] |= cur[j-1]
            prev = cur
        
        return prev[len(s2)]
