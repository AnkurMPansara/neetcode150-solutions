class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob1, rob2 = 0, 0
        rob3, rob4 = 0, 0

        for i in range(len(nums)-1):
            temp1, temp2 = max(nums[i]+rob2,rob1), max(nums[i+1]+rob4, rob3)
            rob1, rob2, rob3, rob4 = temp1, rob1, temp2, rob3
        
        return max(rob1, rob3)

