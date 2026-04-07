class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        prev = 1
        cur = 0
        if s[0] == "1":
            cur += 1
        if s[0] == "2" and s[1] in "0123456":
            cur += 1
        if s[1] != "0":
            cur += 1

        for i in range(2, len(s)):
            temp = 0
            if s[i-1] == "1":
                if s[i] == "0":
                    temp = prev
                else:
                    temp = cur + prev
            elif s[i-1] == "2" and s[i] in "0123456":
                if s[i] == "0":
                    temp = prev
                else:
                    temp = cur + prev
            else:
                if s[i] == "0":
                    temp = 0
                else:
                    temp = cur
            cur, prev = temp, cur
        
        return cur
