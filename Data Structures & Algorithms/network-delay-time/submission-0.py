class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))
        
        heap = [(0, k)]
        visit = set()
        t = 0
        while heap:
            t1, u1 = heapq.heappop(heap)
            if u1 in visit:
                continue
            visit.add(u1)
            t = max(t, t1)
            for v2, t2 in edges[u1]:
                if v2 not in visit:
                    heapq.heappush(heap, (t1+t2, v2))
        return t if len(visit) == n else -1