class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            if len(graph[u]) == 2:
                return u
            if len(graph[v]) == 2:
                return v