class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                val = stack.pop()
                result[val[1]] = i-val[1]
            stack.append([temp, i])
        return result
        