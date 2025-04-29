class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        minheap = []
        heapq.heappush(minheap,(0,0,0))
        res = [[float('inf')]*(cols) for _ in range(rows)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while minheap:
            effort,r,c = heapq.heappop(minheap)
            if r == rows - 1 and c == cols - 1:
                return effort
            for dr,dc in directions:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    diff = abs(heights[r][c]-heights[nr][nc])
                    maxi = max(effort,diff)
                    if res[nr][nc] > maxi:
                        res[nr][nc] = maxi
                        heapq.heappush(minheap,(maxi,nr,nc))
        return 0

            
        