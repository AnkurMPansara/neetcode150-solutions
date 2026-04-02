class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for s in strs:
            v = ''.join(sorted(s))
            if v in store:
                store[v].append(s)
            else:
                store[v] = [s]
        return list(store.values())