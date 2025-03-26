class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                arr.append(grid[i][j])
        arr.sort()
        cnt = 0
        median = arr[len(arr)//2]
        for num in arr:
            diff = abs(num-median)
            if diff % x != 0: return -1
            cnt += diff//x
        return cnt
        