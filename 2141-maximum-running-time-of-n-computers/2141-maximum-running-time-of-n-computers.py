class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def countMax(mid):
            count = 0
            for battery in batteries:
                count += min(battery,mid)
            return count >= n * mid
        
        batteries.sort()
        low = 1
        high = sum(batteries) // n
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if countMax(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
        