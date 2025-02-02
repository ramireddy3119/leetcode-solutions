class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i, visited):
            for j in range(len(isConnected)):  # Check all possible connections
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)  # Mark as visited
                    dfs(j, visited)

        rows = len(isConnected)
        cols = len(isConnected[0])
        Provinces = 0
        visited = set()
        for i in range(rows):
            if i not in visited:
                dfs(i,visited)
                Provinces += 1
        return Provinces
        