class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]
        for u in range(n):
            for v in graph[u]:
                adj[v].append(u)

        indegree = [0] * n
        for u in range(len(adj)):
            for v in adj[u]:
                indegree[v] += 1

        queue = deque([i for i in range(n) if indegree[i] == 0])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        res.sort()
        return res
        