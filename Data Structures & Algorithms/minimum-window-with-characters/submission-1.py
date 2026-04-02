class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_window_substring = ""
        charset_t = [0]*128
        for c in t:
            charset_t[ord(c)] += 1
        charset_s = [0]*128
        l = 0
        matches = 0
        for i in range(128):
            if charset_t[i] == 0:
                matches += 1
        for r in range(len(s)):
            charset_s[ord(s[r])] += 1
            if charset_t[ord(s[r])] == charset_s[ord(s[r])]:
                matches += 1
            while l<len(s) and charset_s[ord(s[l])] > charset_t[ord(s[l])]:
                charset_s[ord(s[l])] -= 1
                l += 1
            if matches == 128:
                if len(min_window_substring) == 0 or len(min_window_substring) > (r-l+1):
                    min_window_substring = s[l:r+1]
        return min_window_substring
