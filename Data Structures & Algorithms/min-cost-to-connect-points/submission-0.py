class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        res = 0
        visit = set()
        heap = [[0, 0]]
        while len(visit) < n:
            cost, pt = heapq.heappop(heap)
            if pt in visit:
                continue
            res += cost
            visit.add(pt)
            for ncost, npt in adj[pt]:
                if npt not in visit:
                    heapq.heappush(heap, [ncost, npt])
        return res