class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_count_s1 = [0]*26
        for c in s1:
            char_count_s1[ord(c) - ord('a')] += 1
        l = 0
        char_count_s2 = [0]*26
        matches = 0
        for i in range(26):
            if char_count_s1[i] == char_count_s2[i]:
                matches += 1
        for r in range(len(s2)):
            char_count_s2[ord(s2[r]) - ord('a')] += 1
            if char_count_s2[ord(s2[r]) - ord('a')] == char_count_s1[ord(s2[r]) - ord('a')]:
                matches += 1
            while len(s1) < (r-l+1):
                if char_count_s2[ord(s2[l]) - ord('a')] == char_count_s1[ord(s2[l]) - ord('a')]:
                    matches -= 1
                char_count_s2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if matches == 26:
                return True
        return False
            
        