class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        left = 1
        right = max(candies)
        best = 0
        while left <= right:
            mid = (left + right) // 2
            totalChild = sum(c // mid for c in candies)
            if totalChild >= k:
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        return best
        