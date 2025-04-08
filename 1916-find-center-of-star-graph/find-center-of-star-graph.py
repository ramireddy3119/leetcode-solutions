class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(len(edges)+2)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        for i in range(len(adj)):
            if len(adj[i]) == len(edges):
                return i
         
        