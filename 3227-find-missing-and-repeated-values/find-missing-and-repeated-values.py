class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        mpp = {}
        repeat = -1
        summ = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in mpp:
                    repeat = grid[i][j] 
                summ += grid[i][j]
                mpp[grid[i][j]] = mpp.get(grid[i][j],0)+1
        n=len(grid)*len(grid[0])
        totSum = n*(n+1) // 2
        if summ > totSum:
            rem = summ - totSum
            return [repeat,repeat-rem]
        else:
            rem = totSum - summ
            return [repeat,repeat+rem]

        

        