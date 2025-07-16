class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        dp = [[0]*2 for _ in range(2)]
        maxi = -1
        for num in nums:
            num %= 2
            for j in range(2):
                y = (j-num+2)%2
                dp[num][y] = 1 + dp[y][num]
                maxi = max(maxi,dp[num][y])
        return maxi
        
        