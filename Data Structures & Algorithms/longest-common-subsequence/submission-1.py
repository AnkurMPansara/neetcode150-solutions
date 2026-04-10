class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        dpPrev = [0]*(len(text2)+1)
        for i in range(len(text1)):
            dpCur = [0]*(len(text2)+1)
            for j in range(1,len(text2)+1):
                if text1[i] == text2[j-1]:
                    dpCur[j] = dpPrev[j-1] + 1
                else:
                    dpCur[j] = max(dpPrev[j], dpCur[j-1])
            dpPrev = dpCur
        
        return dpPrev[-1]