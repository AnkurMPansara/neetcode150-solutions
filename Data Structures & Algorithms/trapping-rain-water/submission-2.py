class Solution:
    def trap(self, height: List[int]) -> int:
        water_area = 0
        l, r = 0, len(height)-1
        l_max = height[l]
        r_max = height[r]
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                water_area += max(l_max - height[l], 0)
            else:
                r -= 1
                r_max = max(r_max, height[r])
                water_area += max(r_max - height[r], 0)
        return water_area