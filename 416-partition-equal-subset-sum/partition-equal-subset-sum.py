class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ%2 != 0:
            return False
        tar = summ // 2
        dp = [False]*(tar+1)
        dp[0] = True
        for num in nums:
            for j in range(tar,num-1,-1):
                dp[j] = dp[j] or dp[j-num]
        return dp[tar]

        