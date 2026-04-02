class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        l = 0
        char_loc = {}
        for r in range(len(s)):
            if s[r] in char_loc:
                l = max(char_loc[s[r]]+1, l)
            char_loc[s[r]] = r
            longest_substring = max(longest_substring, r-l+1)
        return longest_substring