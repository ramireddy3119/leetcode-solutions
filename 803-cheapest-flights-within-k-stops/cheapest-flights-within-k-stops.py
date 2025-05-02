from collections import deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for f, t, p in flights:
            graph[f].append((t, p))
        
        q = deque([(0, (src, 0))])  # Correct syntax
        dist = [float('inf')] * n
        dist[src] = 0

        while q:
            stop, (node, dis) = q.popleft()
            if stop > k:
                continue
            for neighbour, ndis in graph[node]:
                newdis = dis + ndis
                if newdis < dist[neighbour]:
                    dist[neighbour] = newdis
                    q.append((stop + 1, (neighbour, newdis)))
        
        return dist[dst] if dist[dst] != float('inf') else -1
