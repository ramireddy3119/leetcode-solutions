class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colorFreq = {}
        ballColor = {}
        res = []
        for ball, newColor in queries:
            if ball in ballColor:
                oldColor = ballColor[ball]
                colorFreq[oldColor] -= 1
                if colorFreq[oldColor] == 0:
                    del colorFreq[oldColor]
            ballColor[ball] = newColor
            if newColor in colorFreq:
                colorFreq[newColor] += 1
            else:
                colorFreq[newColor] = 1
            res.append(len(colorFreq))
        return res
            