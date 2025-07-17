class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0]*k for _ in range(k)]
        maxi = -1
        for num in nums:
            num %= k
            for j in range(k):
                y = (j-num+k) % k
                dp[num][y] = 1 + dp[y][num]
                maxi = max(maxi,dp[num][y])
        return maxi