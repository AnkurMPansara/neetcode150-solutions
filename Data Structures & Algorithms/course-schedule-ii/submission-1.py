class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)

        res = []
        visit = set()
        cycle = set()

        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            cycle.add(c)
            for p in prereqMap[c]:
                if not dfs(p):
                    return False
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res