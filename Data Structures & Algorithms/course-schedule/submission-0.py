class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i:[] for i in range(numCourses)}
        for course, req in prerequisites:
            prereqMap[course].append(req)
        
        visit = set()

        def dfs(c):
            if c in visit:
                return False
            if len(prereqMap[c]) == 0:
                return True
            
            visit.add(c)
            for p in prereqMap[c]:
                if not dfs(p):
                    return False
            visit.remove(c)
            prereqMap[c] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True