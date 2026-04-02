class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            print(f"temp {temp} stack {stack}")
            while stack and stack[-1][0] < temp:
                val = stack.pop()
                result[val[1]] = i-val[1]
            stack.append([temp, i])
            print(f"stack {stack} result {result}\n")
        return result
        