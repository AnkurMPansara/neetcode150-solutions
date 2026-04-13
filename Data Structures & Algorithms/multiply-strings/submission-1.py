class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = 0

        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                temp = int(num1[i]) * int(num2[j])
                for k in range(i+j):
                    temp *= 10
                res += temp
        
        return str(res)