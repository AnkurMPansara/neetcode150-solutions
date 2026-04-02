class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = { src: [] for src, _ in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            nxtcpy = adj[src]
            for i, v in enumerate(nxtcpy):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i, v)
                res.pop()
            return False
        
        dfs("JFK")
        return res
