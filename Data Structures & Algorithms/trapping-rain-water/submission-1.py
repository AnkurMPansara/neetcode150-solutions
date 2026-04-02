class Solution:
    def trap(self, height: List[int]) -> int:
        water_area = 0
        prefix_max = [0]*len(height)
        postfix_max = [0]*len(height)
        for i in range(1,len(height)):
            prefix_max[i] = max(prefix_max[i-1], height[i-1])
        for i in range(len(height)-2,0,-1):
            postfix_max[i] = max(postfix_max[i+1], height[i+1])
        for i in range(len(height)):
            water_area += max(min(prefix_max[i], postfix_max[i]) - height[i], 0)
        return water_area