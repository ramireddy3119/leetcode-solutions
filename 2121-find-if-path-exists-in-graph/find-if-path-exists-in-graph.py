class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def bfs(graph,start,end):
            visited = [False]*n
            queue = deque([start])
            visited[start] = True
            while queue:
                node = queue.popleft()
                for neighbour in graph[node]:
                    if neighbour == end:
                        return True
                    elif not visited[neighbour]:
                        visited[neighbour] = True
                        queue.append(neighbour)
            return False

        if n == 1:
            return True
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        return bfs(graph,source,destination)
        