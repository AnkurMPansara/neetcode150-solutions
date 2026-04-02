class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif (nums[l] < nums[mid] and nums[mid] > target and nums[l] <= target) or (nums[l] > nums[mid] and (nums[l] <= target or nums[mid] > target)):
                r = mid
            else:
                l = mid+1
        if nums[r] == target:
            return r
        return -1
