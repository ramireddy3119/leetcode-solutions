class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for f,t,p in flights:
            graph[f].append((t,p))
        q = deque([(0,(src,0))])
        dist = [float('inf')]*n
        dist[src] = 0
        while q:
            it = q.popleft()
            stop = it[0]
            node = it[1][0]
            dis = it[1][1]
            if stop > k:
                continue
            for neighbour,ndis in graph[node]:
                newdis = ndis + dis
                if newdis < dist[neighbour] and stop <= k:
                    dist[neighbour] = newdis
                    q.append((stop+1,(neighbour,newdis)))
        return dist[dst] if dist[dst] != float('inf') else -1


