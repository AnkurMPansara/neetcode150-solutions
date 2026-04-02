class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                area = min(heights[i:j+1])*(j-i+1)
                max_area = max(max_area, area)
        return max_area