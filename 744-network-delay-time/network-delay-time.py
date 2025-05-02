class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for u,v,w in times:
            graph[u].append((v,w))
        
        heap = [(0,k)]
        time = [float('inf')]*(n+1)
        time[k] = 0
        while heap:
            t,node = heapq.heappop(heap)
            for neighbour, tt in graph[node]:
                nt = t + tt
                if nt < time[neighbour]:
                    time[neighbour] = nt
                    heapq.heappush(heap,(nt,neighbour))
        max_time = max(time[1:])
        return max_time if max_time != float('inf') else -1


        
        