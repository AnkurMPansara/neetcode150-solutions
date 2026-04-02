class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        bound_r = [0]*len(heights)
        stack = []
        for i in range(len(heights)):
            count = 1
            while stack and heights[stack[-1]] >= heights[i]:
                count += bound_r[stack.pop()]
            bound_r[i] = count
            stack.append(i)
        bound_l = [0]*len(heights)
        stack = []
        for i in range(len(heights)-1, -1, -1):
            count = 1
            while stack and heights[stack[-1]] >= heights[i]:
                count += bound_l[stack.pop()] 
            bound_l[i] = count
            stack.append(i)
        for i in range(len(heights)):
            max_area = max(max_area, (bound_r[i]+bound_l[i]-1)*heights[i])
        return max_area