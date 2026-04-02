class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_substring = 0
        l = 0
        charset = {}
        most_freq_char = s[0]
        total_char = 0
        for r in range(len(s)):
            if s[r] in charset:
                charset[s[r]] += 1
            else:
                charset[s[r]] = 1
            if charset[s[r]] >= charset[most_freq_char]:
                most_freq_char = s[r]
            total_char += 1
            while total_char - charset[most_freq_char] > k:
                charset[s[l]] -= 1
                total_char -= 1
                l += 1
                if s[l] == most_freq_char:
                    max_freq = 0
                    for char, freq in charset.items():
                        if freq >= max_freq:
                            most_freq_char = char
                            max_freq = freq
            longest_substring = max(longest_substring, r-l+1)
        return longest_substring
                

        