class Solution:
    def isPalindrome(self, s: str) -> bool:
        flitered_string = ""
        for c in s:
            if c.isalnum():
                flitered_string += c
        s = flitered_string.lower()
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True