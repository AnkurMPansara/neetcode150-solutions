class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        window = []
        for i in range(k-1):
            heapq.heappush(window, (-nums[i], i))
        for l in range(len(nums)-k+1):
            heapq.heappush(window, (-nums[l+k-1], l+k-1))
            while window and window[0][1] < l:
                heapq.heappop(window)
            print(window)
            answer.append(-window[0][0])
        return answer