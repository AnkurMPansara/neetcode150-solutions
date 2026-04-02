class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        three_sum = []
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                s = nums[i]+nums[j]+nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    three_sum.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j<k:
                        j += 1
                    
        return list(three_sum)
        