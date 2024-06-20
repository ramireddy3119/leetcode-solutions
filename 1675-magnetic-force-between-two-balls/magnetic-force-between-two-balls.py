class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def isOkAtDis(position:List[int],m,mid) ->bool:
            ballAtPlaced = 1
            prevEle = 0
            for i in range(1,len(position)):
                if position[i] - position[prevEle] >= mid:
                    ballAtPlaced += 1
                    prevEle = i
            return ballAtPlaced >= m
        position.sort()
        low = 0
        high = position[-1]
        ans = -1
        while low <= high:
            mid = (low + high)//2
            if isOkAtDis(position,m,mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

