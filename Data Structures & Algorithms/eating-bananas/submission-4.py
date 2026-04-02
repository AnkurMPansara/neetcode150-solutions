class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l<r:
            print(f"l: {l} r: {r}")
            mid = (l+r)//2
            hl = sum([math.ceil(pile/l) for pile in piles])
            hm = sum([math.ceil(pile/mid) for pile in piles])
            hr = sum([math.ceil(pile/r) for pile in piles])
            if hm > h:
                l = mid+1
            else:
                r = mid
        print(f"final l: {l} r: {r}")
        return (l+r)//2
        