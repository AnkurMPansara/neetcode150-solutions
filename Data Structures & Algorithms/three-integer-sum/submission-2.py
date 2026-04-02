class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        three_sum = []
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                s = nums[i]+nums[j]+nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    if [nums[i], nums[j], nums[k]] not in three_sum:
                        three_sum.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    
        return list(three_sum)
        