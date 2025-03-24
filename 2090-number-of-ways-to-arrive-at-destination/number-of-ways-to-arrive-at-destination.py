class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7 
        graph = defaultdict(list)
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        pq = [(0, 0)]
        dist = {node: float('inf') for node in range(n)}
        count = {node: 0 for node in range(n)}

        dist[0] = 0
        count[0] = 1

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in graph[u]:
                new_dist = d + w

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    count[v] = count[u] % MOD
                    heapq.heappush(pq, (new_dist, v))

                elif new_dist == dist[v]:
                    count[v] = (count[v] + count[u]) % MOD

        return count[n-1] % MOD
