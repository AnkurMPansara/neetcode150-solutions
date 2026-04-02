class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += ".".join(str(ord(c)) for c in s) + ","
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_list = []
        word = ""
        char = ""
        for c in s:
            if c == ".":
                if char:
                    word += chr(int(char))
                char = ""
            elif c == ",":
                if char:
                    word += chr(int(char))
                    char = ""
                decoded_list.append(word)
                word = ""
            else:
                char += c
        return decoded_list