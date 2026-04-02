class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        order = sorted(counter, key=lambda k:counter[k], reverse=True)
        return order[:k]