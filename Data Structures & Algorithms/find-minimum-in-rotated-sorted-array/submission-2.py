class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            ans = min(ans, nums[mid])
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        ans = min(ans, nums[r])
        return ans